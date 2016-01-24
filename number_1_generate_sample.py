'''
Purpose: 
	Generate file which containt numbers (assume 1 to 255 - 1 byte/8 bits) for test
	Example output file 'age.txt':
	============================
	23
	51
	35
	...
	============================

Method:
	Generate random numbers

Sample execution: 
	python number_1_generate_sample.py <size_number> <file_output>
	python number_1_generate_sample.py 1000000 'age.txt'
'''

import sys
import random
import time

start_time = time.time() #start count the time

size_number = int(sys.argv[1])
file_output = str(sys.argv[2])

def main():
    numbers = []

    infile = open (file_output, 'w')

    for n in range(1,size_number):
        numbers.append(random.randint(1,255))
    infile.write('\n'.join(map(str, numbers)))
    infile.close()
main()

elapsed_time = time.time() - start_time #get the time
print 'output = ', file_output, ', elapsed time: ', str(elapsed_time) #print the time