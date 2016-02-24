import nsfg
import thinkstats2

def Mode(hist):
	"""return the mode of histogram
	"""
	mode = 0
	mode_freq = 0
	for value, freq in hist.Items():
		if  freq > mode_freq:
			mode = value
			mode_freq = freq
	return mode
