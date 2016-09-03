import nsfg
import first
import thinkstats2
import thinkplot
import numpy as np

df = nsfg.ReadFemPreg()

def ScatterPlot():    
    thinkplot.Scatter(df.agepreg, df.totalwgt_lb)
    thinkplot.Show(xlabel = 'Age (years)',
                   ylabel = 'Weight (lb)',
                   xlim = [10, 45],
                   ylim = [0, 15],
                   legend = False)

def BinnedPercentiles():
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)
    
    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]
    
    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label = label)
        
    thinkplot.Save(root = 'chap07scatter3',
               formats = ['jpg'],
               xlabel = 'mother\'s age (years)',
               ylabel = 'birth weight (lbs)')

def Correlation():
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset = ['agepreg', 'totalwgt_lb'])
    
    ages = live.agepreg
    weights = live.totalwgt_lb
    print('Pearson\'s Correlation', thinkstats2.Corr(ages, weights))
    print('Spearman\'s Correlation', thinkstats2.SpearmanCorr(ages, weights))