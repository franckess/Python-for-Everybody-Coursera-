### Assignment: Counting Organizations

# This application will read the mailbox data (mbox.txt) count up the number email messages per organization 
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
# Alternative option: using the url 'http://www.pythonlearn.com/code/mbox.txt'

import sqlite3
import re
import urllib

conn = sqlite3.connect('emaildb_V2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


cur.execute('DELETE FROM Counts')
counts = dict()
fh = urllib.urlopen('http://www.pythonlearn.com/code/mbox.txt')
for line in fh:
    pieces = line.strip()
    org = re.findall('^From.+@(.+?\s{1})', pieces)
    if len(org) == 0 : continue
    counts[org[0].rstrip()] = counts.get(org[0].rstrip(),0) + 1

for key,val in counts.items():
    cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, ? )''', ( key, val) )
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()