# -*- coding:utf8 -*-

from operator import add

#print filter(int,'123'[0]),type(filter(int,'123'[0]))
print filter(int,'123'),type(filter(int,'123'))

print map(int,['1','2','3']),type(map(int,[1,2,3]))

print reduce(add,'123','a'),type(reduce(add,'123','a'))

'''
#map
def add(obj):
    return obj+1
print map(add,[1,2,3])
print map(lambda x,y:x+y,[1,2,3],[10,10,10])

#reduce
from functools import reduce
def str1int(s):
    def fn(x, y):
        return x * 10 + y

    def char1num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char1num, s))
print str1int('1')
'''

