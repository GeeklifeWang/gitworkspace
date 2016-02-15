# -*- coding:utf8 -*-
#生成器

f = (x * x for x in range(10))
#print f.next()
#for i in f:print i


def generator(list1=[0,1,2,3,4,5]):
    for i in list1:
        yield i

g = generator()
print g.next()

for i in generator():
    print i
