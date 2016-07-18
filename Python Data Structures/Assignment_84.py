
fname = raw_input("Enter file name: ")
path = 'E:/Coursera/Python-for-Everybody-Coursera/Python Data Structures/'
filename = path + fname


try:
    fh = open(fname)
except:
    print 'The following file doesn''t exist:',fname
    exit()

lst = list()
for line in fh:
    newline = line.split()
    m = len(newline)
    len_range = range(m)
    for i in len_range:
        value = newline[i]
        if value not in lst:
        	lst.append(value)
lst.sort()
print lst