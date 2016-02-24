import nsfg
import thinkstats2
import thinkplot
from operator import itemgetter

def Mode(hist):
	"""Return the mode of histogram
	"""
	mode = 0
	mode_freq = 0
	for value, freq in hist.Items():
		if  freq > mode_freq:
			mode = value
			mode_freq = freq
	return mode

def AllModes(hist):
	"""Return all modes of histogram
	as a list of value-frequency pairs in descending order
	or frequency
	"""
	return sorted(hist.Items(), key=itemgetter(1), reverse=True)

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def WeightDifference(live, firsts, others):
	
	mean_all = live.totalwgt_lb.mean()
	mean_firsts = firsts.totalwgt_lb.mean()
	mean_others = others.totalwgt_lb.mean()
	var_firsts = firsts.totalwgt_lb.var()
	var_others = others.totalwgt_lb.var()
	std_firsts = firsts.totalwgt_lb.std()
	std_others = others.totalwgt_lb.std()
	
	print('Mean')
	print('Firsts', mean_firsts)
	print('Others', mean_others)
	
	print('Variance')
	print('Firsts', var_firsts)
	print('Others', var_others)
	
	print('Standard Deviation')
	print('First', std_firsts)
	print('Others', std_others)
	
	print('Difference in lbs')
	print(mean_firsts - mean_others)
	
	print('Difference relative to mean in %')
	print((mean_firsts - mean_others) / mean_all * 100, '%')
	
	print('Cohen\'s d')
	print(thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
