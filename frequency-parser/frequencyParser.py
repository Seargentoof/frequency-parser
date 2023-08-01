"""
Functions and algorithms for parsing medical Frequencies. 

Dawson Lin, 7/28/2023
"""


#### Methods


"""
Returns the hour equivalent of a frequency. 
"""
def hour_equivalent(frequency: str) -> float:
	pass
	#1. frequencyIdentifiers = list containing all identifiers (e.g, bid, ac, biwk, every, q,
	# 	daily, nx where n is a number) in the frequency
	#	frequencyUnit = the frequency's unit of time (e.g, minute, hour)
	#	frequencyCustomTimes = list containing miscellaneous info presented in the 
	# 	frequency. (e.g. /mon/tu/wed/, which are days of the week listed to take 
	# 	the medicine.) NOTE: worry about this later. 

	
	#2. hourEquivalent = None

	#3. if frequencyIdentifiers contains "n doses per t period of time" identifiers like bid, 
	# 	ac, or biwk
	#		a. n = number of doses; t = the period of time, in hours, in which those doses 
	#		occur (i.e, 2 times a day = 2 times every 24 hours)
	#		b. hourEquivalent = t/n to gain the number of hours that elapse before another  
	#		dose is taken

	#4. if frequencyIdentifiers contains "1 dose every t time" identifiers like q or
	#	every
	#		a. hourEquivalent = t converted to hours 
	# 		(i.e, 3 days = 72 hours; 1 minute = 1/60 hours)

	#5. if frequencyCustomTimes is not empty, perform calculations on the hourEquivalent 
	#	as necessary. NOTE: worry about this later. 

	#6. if hourEquivalent is still None, print "Unable to calculate hourEquivalent."

	#7. return hourEquivalent


#### Implementation
"""
Takes two string frequencies and determines whether they are equal.
"""
def frequencies_are_equal(frequency1: str, frequency2: str) -> bool:
	pass
	#1. return whether the hour equivalent of frequency1 equals that of frequency2
	#	(NOTE: beware of comparing floats for equality)
	



