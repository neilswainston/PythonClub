'''
PythonClub (c) University of Manchester 2018

All rights reserved.

@author: neilswainston
'''
my_file = open('my_filename.txt', 'r')

for line in my_file:
    print(line.strip())

my_file.close()
