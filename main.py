#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import glob
import numpy


# List "lst" files in current folder
sets = glob.glob("*.lst")
print(sets)

# Randomly select a set
myset = numpy.random.choice(sets)
print(myset)

# open read selected set
select_set = [line.rstrip('\n') for line in open(myset)]
#print(select_set)


# Randomly choose items from selected set
choice_size = numpy.random.choice([1,2,3])
#print(choice_size)
choice = numpy.random.choice(select_set, size=choice_size, replace=False)
print(choice)
