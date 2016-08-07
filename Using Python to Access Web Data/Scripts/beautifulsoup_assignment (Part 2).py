### Assignment: Following Links in Python

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and 
# report the last name you find.
# 
# We provide two files for this assignment. 
# One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
# 
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Argyll.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')

count = 0
link = list()
link.append(url)
pos = 18 # position of the link
total_iter = 7 # number of iterations
count = 0

while count < total_iter:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	# Retrieve all of the 'span' tags
	tags = soup.findAll('a')
	if len(tags) < pos:
		break
	tag_a = tags[pos-1].get('href', None)
	link.append(tag_a)
	url = str(tag_a)
	count += 1

print 'Enter count:', total_iter
print 'Enter position:', pos
for l in link:
	print 'Retrieving: ', l