'''
Env: python 2.7.6
Purpose: 
	Generate a list of 1 Million blacklisted name and phone number. Each line is one word(name), followed by space, then the phone number.
	Example blacklist.txt:
	============================
	Andi 1341441
	Melisa 8565467
	Aslam 2908345
	...
	============================

Method:
	Generate random name and phonenumber_generator

Sample execution: 
	python number_3_generate_sample.py <size_number> <file_output>
	python number_3_generate_sample.py 1000000 'blacklist.txt'
'''

import sys
import random
import time
import string

start_time = time.time() #start count the time

size_number = int(sys.argv[1])
file_output = str(sys.argv[2])

def name_generator(size=6, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def phonenumber_generator(size=8, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def main():
    numbers = []

    infile = open (file_output, 'w')

    for n in range(1,size_number):
    	name = name_generator()
    	phonenumber = phonenumber_generator()
        numbers.append(str(name) +' '+ str(phonenumber))
    infile.write('\n'.join(map(str, numbers)))
    infile.close()
main()

elapsed_time = time.time() - start_time #get the time
print 'output = ', file_output, ', elapsed time: ', str(elapsed_time) #print the time