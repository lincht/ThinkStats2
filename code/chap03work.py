import nsfg
import thinkstats2
import thinkplot

# Exercise 3.2
def PmfMean(pmf):
    mean = 0
    for x, p in pmf.Items():
        mean += p * x
    return mean

def PmfVar(pmf):
    var = 0
    mean = PmfMean(pmf)
    for x, p in pmf.Items():
        var += p * ((x - mean) ** 2)
    return var

# Exercise 3.3
df = nsfg.ReadFemPreg()
live = df[df.outcome == 1]
live = live[live.prglngth >= 37]
preg_map = nsfg.MakePregMap(live)

def Diffs(list):
    first = list[0]
    rest = list[1:]
    diffs = [first - x for x in rest]
    return diffs
    
def PairWiseDifference(live):
    
    diffs = []
    
    for id, list_indices in preg_map.items():
        prglngths = live.loc[list_indices].prglngth.values
        if len(prglngths) >= 2:
            diffs.extend(Diffs(prglngths))
    
    mean = thinkstats2.Mean(diffs)
    print('mean difference between pairs', mean)
    
    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='difference in weeks', ylabel='PMF')

# Exercise 3.4
import relay

def ObservedPmf(pmf, ob_speed, label=None):
    observed = pmf.Copy(label=label)
    for speed, prob in observed.Items():
        diff = abs(ob_speed - speed)
        observed.Mult(speed, diff)
        observed.Normalize()
    return observed

results = relay.ReadResults()
speeds = relay.GetSpeeds(results)
bin = relay.BinData(speeds, 3, 12, 100)

pmf = thinkstats2.Pmf(bin, label='actual speeds')
observed = ObservedPmf(pmf, 7.5, label='observed speeds')

thinkplot.Pmf(observed)
thinkplot.Show(xlabel='speed', ylabel='PMF')
