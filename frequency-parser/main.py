"""
Entry point for frequencyParser.

Dawson Lin, 7/28/2023
"""

import frequencyParser as parser
import utilities as util
import time

print('Check for correctness:', parser.frequencies_are_equal('tu/ w/f/sa/su', 'tu/ w/f/sa/su'))
print('Check for correctness:', parser.frequencies_are_equal('q shift', 'q 12hr'))
print('Check for correctness:', parser.frequencies_are_equal('Tu/W/f/Sa/Su', 'tu/w/f/sa/su'))
print('Check for correctness:', parser.frequencies_are_equal('Q SHIFT', 'q 12 hr'))

def time_operation(data1Num, data2Num):
	orders1 = util.read_file_lines("input/" + data1Num + ".data")
	orders2 = util.read_file_lines("input/" + data2Num + ".data")

	num = len(orders1)

	startTime = time.time()

	for i in range(0, num): 
		try:
			parser.frequencies_are_equal(orders1[i], orders2[i])
		except: 
			continue

	endTime = time.time()
	elapsedTime = endTime - startTime

	print("Elapsed time:", elapsedTime, "seconds")
	print("Order pairs compared: " +  str(num))

print()
time_operation('01a', '01a')
print()
time_operation('01b','01b')
print()
time_operation('01b','01c')