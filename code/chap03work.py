import nsfg
import thinkstats2

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_pmf = thinkstats2.Pmf(firsts.prglngth)
other_pmf = thinkstats2.Pmf(others.prglngth)

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

#Exercise 3.3
