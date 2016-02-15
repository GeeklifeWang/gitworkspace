#-*- coding:utf-8 -*-

f = open('1.txt','w')
f.seek(2,0)
print f.tell()
#print f.truncate()
f.write('asdhafnajks')
f.writelines(x+'\n' for x in 'asdhafnajks')
print f.name

print '指针%s' % f.tell()
f.seek(100,2)
print '指针%s' % f.tell()

for line in f:
    line = line.strip('\n\r').split(' ')
    print line
    for i in line:
        if i != '':
            print i,
    print
#print '指针%s' % f.tell()
f.close()

