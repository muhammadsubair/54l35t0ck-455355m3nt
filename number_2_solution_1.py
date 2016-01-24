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
     Assume the every age is 1 byte (using unsigned integer is range from 0 - 255). RAM size is 1 GB = 1,073,741,824 byte (and partly used by another process :D). The size of 7Billion age is around 7,000,000,000 , so it would not enough in RAM.
     The reference is from Guido van Rosum's blog post, with almost similar problem (except the size of file and RAM) http://neopythonic.blogspot.co.id/2008/10/sorting-million-32-bit-integers-in-2mb.html . 
     The main idea is have to be some kind of merge sort, where small chunks of the data are sorted in memory and written to a temporary file, and then the temporary files are merged into the eventual output area. 

Sample execution:
    python number_1_solution_1.py <file_input> <file_output>
    python number_1_solution_1.py 'age.txt' 'sorted_age.txt'
'''
import sys
import time
import sys, array, tempfile, heapq
assert array.array('i').itemsize == 4

start_time = time.time() #start count the time

file_input = str(sys.argv[1])
file_output = str(sys.argv[2])

def intsfromfile(f):
  while True:
     a = array.array('i')
     a.fromstring(f.read(4000))
     if not a:
         break
     for x in a:
         yield x

iters = []
while True:
  a = array.array('i')
  a.fromstring(sys.stdin.buffer.read(40000))
  if not a:
      break
  f = tempfile.TemporaryFile()
  array.array('i', sorted(a)).tofile(f)
  f.seek(0)
  iters.append(intsfromfile(f))

a = array.array('i')
for x in heapq.merge(*iters):
  a.append(x)
  if len(a) >= 1000:
      a.tofile(sys.stdout.buffer)
      del a[:]
if a:
  a.tofile(sys.stdout.buffer)

elapsed_time = time.time() - start_time #get the time
print 'output = ', file_output, ', elapsed time: ', str(elapsed_time) #print the time