## Assignment 111

# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

name = raw_input("Enter file:")
path = 'E:/Coursera/Python-for-Everybody-Coursera/Using Python to Access Web Data/Data/'
name = path + name

try:
    handle = open(name)
except:
    print 'The following file doesn''t exist:', name
    exit()

sum = 0
for line in handle:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	if len(x) == 0: continue
	for num in x:
		sum = sum + int(num)
print sum

