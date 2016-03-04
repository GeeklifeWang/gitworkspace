#-*- cofing:utf8 -*-
# *将序列参数unpack

def f(*arg):
    print arg

l1 = [1,2,3]
l2 = [4,5,6]

f(l1)
f(l1,l2)
f(*(l1+l2))
