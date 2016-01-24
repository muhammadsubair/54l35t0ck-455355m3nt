'''
Purpose: 
    Solve question number 1;
    You are given a textfile that contains the age (Integer) of each people in Jakarta, let's assume Jakarta 10 Million people. The format of the file is very simple, each line is an integer representing age of one people.

    Example age.txt:
    ============================
    23
    51
    35
    ============================

    Write a script/program in Python or Java or Scala that takes this file name as an input, and produce an output file that contains the sorted age in the same format. You are not allowed to use any external library besides the built-in library for the language that you choose.

    Example sorted_age.txt:
    ============================
    23
    35
    51
    ============================

Methond:
    Using python sort() (faster than using sorted());

Sample execution:
    python number_1_solution_1.py <file_input> <file_output>
    python number_1_solution_1.py 'age.txt' 'sorted_age.txt'
'''
import sys
import time

start_time = time.time() #start count the time

file_input = str(sys.argv[1])
file_output = str(sys.argv[2])

# file_input = 'age.txt'
# file_output = 'sorted_age.txt'

def main():
    ages = []
    with open(file_input, 'r') as f:
        for line in f:
            ages.append(int(line))

    ages.sort()
    # sorted_ages = quickSort(ages)

    numbers = []
    infile = open(file_output, 'w')
    for age in ages:
        # print age
        numbers.append(age)
    infile.write('\n'.join(map(str, numbers)))
    infile.close()
main()

elapsed_time = time.time() - start_time #get the time
print 'output = ', file_output, ', elapsed time: ', str(elapsed_time) #print the time