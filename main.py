#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import glob
import numpy
import os

#> List "lst" files in current folder
full_path = os.path.realpath(__file__) 
cur_dir = os.path.dirname(full_path)
#print(cur_dir)
sets = glob.glob(cur_dir + "/*.lst")
#print(sets)


again = 1

while again:


    #> Randomly select a set
    myset = numpy.random.choice(sets)
    #print(myset)
    
    #> open read selected set
    select_set = [line.rstrip('\n') for line in open(myset)]
    #print(select_set)
    
    #> Randomly choose items from selected set
    choice_size = numpy.random.choice([1,2,3])
    #print(choice_size)
    choice = numpy.random.choice(select_set, size=choice_size, replace=False)
    print(choice)

    is_again = raw_input("Press 'enter' to re-do ir again: ")
    if is_again != "":
        again = 0


