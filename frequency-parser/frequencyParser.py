"""
Functions and algorithms for parsing medical Frequencies. 

Dawson Lin, 7/28/2023
"""

import pandas as pd
import math
import numpy

#### Methods

"""
Loads the data from the xlsx file in filepath and returns it as a sorted dictionary.

Precondition: xlsx file must be a file consisting of frequency expressions 
"""
def load_xlsx_file_to_dictionary(filepath = 'information/frequencies.xlsx', 
	column1 = 'frequency', column2 = 'hour equivalent') -> dict:
	pass
	# load the file into a variable df
	df = pd.read_excel(filepath)

	# create a new dictionary result
	result = dict()

	# for each row in the spreadsheet from index 1 onwards 
	#	add to result (key = element in the frequency column, value = corresponding
	#	hour equivalent)
	for index, row in df.iterrows():
		result.update({row[column1]: row[column2]})
	
	
	# sort result by key pairs in alphabetical order
	sortedKeys = sorted(result.keys())
	sortedDict = {key: result[key] for key in sortedKeys}
	result = sortedDict

	# strip the dictionary of spaces and make everything lowercase
	result = standardize(result)

	# return result
	return result


"""
Strips all of the keys in dictionary of spaces and makes everything lowercase
Precondition: the key must be a frequency expression
"""
def standardize(dictionary: dict) -> dict:
	SPACE = " " # constants

	result = dict()

	for frequency in dictionary.items():
		key = frequency[0]
		key = key.strip()
		key = key.replace(SPACE, "")
		key = key.lower()
		value = frequency[1]
		result[key] = value

	return result

# dictionary for frequencyParser
frequencyDictionary = load_xlsx_file_to_dictionary()
#print(frequencyDictionary)


#### Implementation
"""
Takes two string frequencies and determines whether they are equal.
"""
def frequencies_are_equal(frequency1: str, frequency2: str) -> bool:
	global frequencyDictionary #global vars
	SPACE = " " # Constants


	#1. return whether the hour equivalent of frequency1 equals that of frequency2
	#	(NOTE: remember to strip the frequency expressions of spaces and convert e
	# 	everything to lower case)
	#	(NOTE: beware of comparing floats for equality)
	try: 
		val1 = frequencyDictionary.get(frequency1.strip().replace(SPACE, "").lower()) 
		val2 = frequencyDictionary.get(frequency2.strip().replace(SPACE, "").lower())
		if math.isclose(float(val1), float(val2)): return True
		if val1 == val2: return True
		if str(val1) == 'nan' and str(val2) == 'nan': return True #if the hour equivalent is NaN
		return False
	
	except: 
		print("Frequency not found.")
		return False
	


