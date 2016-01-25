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
     Ref from https://raw.githubusercontent.com/spiralout/external-sort/master/extsort.py

Sample execution:
    python number_2_solution_1.py <file_input>
    python number_2_solution_1.py 'age.txt'

Output <file_input>.out
'''
import sys
import time

start_time = time.time() #start count the time

file_input = str(sys.argv[1])
# file_output = str(sys.argv[2])

#
# Sort large text files in a minimum amount of memory
#
import os
import sys
import argparse

class FileSplitter(object):
    BLOCK_FILENAME_FORMAT = 'block_{0}.dat'

    def __init__(self, filename):
        self.filename = filename
        self.block_filenames = []

    def write_block(self, data, block_number):
        filename = self.BLOCK_FILENAME_FORMAT.format(block_number)
        file = open(filename, 'w')
        file.write(data)
        file.close()
        self.block_filenames.append(filename)

    def get_block_filenames(self):
        return self.block_filenames

    def split(self, block_size, sort_key=None):
        file = open(self.filename, 'r')
        i = 0

        while True:
            lines = file.readlines(block_size)

            if lines == []:
                break

            if sort_key is None:
                lines.sort()
            else:
                lines.sort(key=sort_key)

            self.write_block(''.join(lines), i)
            i += 1

    def cleanup(self):
        map(lambda f: os.remove(f), self.block_filenames)

class NWayMerge(object):
    def select(self, choices):
        min_index = -1
        min_str = None

        for i in range(len(choices)):
            if min_str is None or choices[i] < min_str:
                min_index = i

        return min_index

class FilesArray(object):
    def __init__(self, files):
        self.files = files
        self.empty = set()
        self.num_buffers = len(files)
        self.buffers = {i: None for i in range(self.num_buffers)}

    def get_dict(self):
        return {i: self.buffers[i] for i in range(self.num_buffers) if i not in self.empty}

    def refresh(self):
        for i in range(self.num_buffers):
            if self.buffers[i] is None and i not in self.empty:
                self.buffers[i] = self.files[i].readline()

                if self.buffers[i] == '':
                    self.empty.add(i)

        if len(self.empty) == self.num_buffers:
            return False

        return True

    def unshift(self, index):
        value = self.buffers[index]
        self.buffers[index] = None

        return value

class FileMerger(object):
    def __init__(self, merge_strategy):
        self.merge_strategy = merge_strategy

    def merge(self, filenames, outfilename, buffer_size):
        outfile = open(outfilename, 'w', buffer_size)
        buffers = FilesArray(self.get_file_handles(filenames, buffer_size))

        while buffers.refresh():
            min_index = self.merge_strategy.select(buffers.get_dict())
            outfile.write(buffers.unshift(min_index))

    def get_file_handles(self, filenames, buffer_size):
        files = {}

        for i in range(len(filenames)):
            files[i] = open(filenames[i], 'r', buffer_size)

        return files

class ExternalSort(object):
    def __init__(self, block_size):
        self.block_size = block_size

    def sort(self, filename, sort_key=None):
        num_blocks = self.get_number_blocks(filename, self.block_size)
        splitter = FileSplitter(filename)
        splitter.split(self.block_size, sort_key)

        merger = FileMerger(NWayMerge())
        buffer_size = self.block_size / (num_blocks + 1)
        merger.merge(splitter.get_block_filenames(), filename + '.out', buffer_size)

        splitter.cleanup()

    def get_number_blocks(self, filename, block_size):
        return (os.stat(filename).st_size / block_size) + 1

def parse_memory(string):
    if string[-1].lower() == 'k':
        return int(string[:-1]) * 1024
    elif string[-1].lower() == 'm':
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == 'g':
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        return int(string)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',
                        '--mem',
                        help='amount of memory to use for sorting',
                        default='100M')
    parser.add_argument('filename',
                        metavar='<filename>',
                        nargs=1,
                        help='name of file to sort')
    args = parser.parse_args()

    sorter = ExternalSort(parse_memory(args.mem))
    sorter.sort(args.filename[0])


if __name__ == '__main__':
    main()
elapsed_time = time.time() - start_time #get the time
print 'output = ', file_input + '.out, elapsed time: ', str(elapsed_time) #print the time