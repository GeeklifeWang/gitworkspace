#encoding=utf-8
'makeTextFile.py -- create texy file'

import os
ls=os.linesep
import commands

#get filename
#fname='1.txt'
fname='%s.txt' % raw_input('enter file name:')
while True:
    if os.path.exists(fname):
        print ('ERROR: %s already exists\n' % fname)*10
        break
    else:
        break
str1 = ''
str1 = commands.getoutput('')
print str1
f = open(fname,'w')
f.writelines(str1)
f.close
'''
#get file content (text) lines
all=[]
print "\nEnter lines ('.'by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'


#read
#fname = raw_input('name:')+'.txt'
try:
    fobj = open (fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    for eachline in fobj:
        print eachline,
    fobj.close()
'''
