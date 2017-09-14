#coding:utf-8
import time
'''
针对一个函数多次使用的装饰器要写成内部闭包的模式(deco1)，这样返回的是函数对象，在调用的时候执行callable
deco2写法不推荐，这种修饰函数的写法，等于直接执行语句 deco2(func) ,可能与期望不符，切记
'''
def deco1(func):
    def _deco(arg):
        rst = func(arg)
        print time.ctime()
        return rst
    return _deco

@deco1
def myfunc(arg):
    if type(arg) == str:
        print 'bingo'
        return True
    else:
        print 'nope'
        return False

print '---------------------'
myfunc('ss')
myfunc(1)
print '---------------------'

def deco2(func):
    print time.ctime()
    return func

@deco2
def myfunc1():
    print '111'
    return False

print '###############'
myfunc1()
myfunc1()
print '###############'

@deco2
def myfunc2():
    print '222'
    return False
myfunc2()
