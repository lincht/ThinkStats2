import nsfg
import thinkstats2

def Mode(hist):
	"""return the mode of histogram
	"""
	mode = 0
	freq = 0
	for value, freq in hist.Items():
		if freq > freq:
			mode = value
			freq = freq
	return mode
