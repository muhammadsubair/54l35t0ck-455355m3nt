'''
Env: python 2.7.6
Purpose: 
    Solve question number 2;
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

    If age.txt contains the age of not only people in Jakarta, but the whole world (7 Billion People). Also, you only have a shitty laptop with 1GB of RAM. Can your script in part 1 handle this file? If not, how would you modify it so it can handle this kind of big file?

Methond:
     Assume the every age is 1 byte (using unsigned integer is range from 0 - 255). RAM size is 1 GB = 1,073,741,824 byte (and partly used by another process). The size of 7Billion age is around 7,000,000,000 , so it would not enough in RAM.
     Ref https://gist.githubusercontent.com/arunenigma/8177109/raw/b951843d35335c8516b3cfbe456592974c32d76c/sort_mill.py, which also inspired by http://neopythonic.blogspot.co.id/2008/10/sorting-million-32-bit-integers-in-2mb.html

Sample execution:
    python number_2_solution_1.py <file_input>
    python number_2_solution_1.py 'age.txt'

Output <file_input>.out
'''
import sys
import time
import array
import heapq
import random
import struct
import tempfile

start_time = time.time() #start count the time

file_input = str(sys.argv[1])
file_output = str(sys.argv[2])

# assertion throws an exception when integers are 64 bit i.e. 8 bytes
# passes since my mac uses 4 bytes = 32 bits for integers | i -> signed int
assert(array.array('i').itemsize == 4)
# refer array module docs

# convert input to format array 32 bits
with open('inp.dat', 'wb') as inp:
    # for _ in xrange(1000000):
    with open(file_input, 'r') as f:
        for line in f:
            # ages.append(int(line))
            integer = int(line)
            b = struct.pack('i', integer)
            inp.write(b)


def get_integers_from_file(tf):
    while True:
        arr = array.array('i')
        arr.fromstring(tf.read(800000))  # 200000 integers of 4 bytes each = 800000 bytes
        if not arr:
            break
        for i in arr:
            yield i

iters = []
inp = open('inp.dat', 'rb')
while True:
    a = array.array('i')
    a.fromstring(inp.read(800000))
    if not a:
        break
    f = tempfile.TemporaryFile()
    array.array('i', sorted(a)).tofile(f)
    f.seek(0)  # go to the zeroth bit
    iters.append(get_integers_from_file(f))

a = array.array('i')
out = open(file_output, 'wb')
for x in heapq.merge(*iters):
    a.append(x)
out.write('\n'.join(map(str, a)))
out.close()

elapsed_time = time.time() - start_time #get the time
print 'output = ', file_output, ', elapsed time: ', str(elapsed_time) #print the time