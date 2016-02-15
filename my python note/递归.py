# -*- coding:utf8 -*-

#递归  该函数包含了对自己本身的调用
def f(x):
    if x==0 or x==1:
        return 1
    else:
        return (x*f(x-1))
print f(5)
