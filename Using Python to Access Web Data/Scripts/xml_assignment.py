### Assignment: Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.
# 
# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# 
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_290590.xml (Sum ends with 19)
# You do not need to save these files to your folder since your program will read the data directly from the URL. 
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_290590.xml'

print 'Enter location:', url

hxml = urllib.urlopen(url).read()

print 'Retrieving', url

print 'Retrieved', len(hxml),'characters'

tree = ET.fromstring(hxml)

sum = 0

count = 0

for item in tree.findall('.//count'):
    sum = sum + int(item.text)
    count += 1

print 'Count: ', count
print 'Sum: ', sum