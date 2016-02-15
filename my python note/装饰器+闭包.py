# -*- coding:utf8 -*-
'''
装饰器
def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco
#mufunc()=deco(myfunc)
def myfunc():
    print("myfunc() called.")
    return 'ok'

myfunc()
'''
'''
#带参数函数的装饰器
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("after myfunc() called. result: %s" % ret)
        return ret
    return _deco

@deco
def myfunc(a, b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)
'''
'''
#多参数函数的装饰器
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@deco
def myfunc2(*args, **kwargs):
    print args,kwargs
    return sum(args)

myfun(1,3)
myfunc2(1,2,3,c=4)
'''
'''
#装饰器带参数
def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print("myfunc() called.")

@deco("module2")
def myfunc2():
    print("myfunc2() called.")

myfunc()
myfunc2()
'''
'''
#装饰器带类参数
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        a=0
        print("locker.acquire() called.这是静态方法:%d" % a)

    @staticmethod
    def release():
        b=1
        print("locker.release() called.不需要对象实例:%d" % b)

def deco(cls):
    #cls 必须实现acquire和release静态方法
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfunc():
    print("myfunc() called.")

myfunc()
'''
class mylocker(object):
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("mylocker.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("lockerex.unlock() called.")

def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco

@lockhelper(mylocker)
def myfunc():
    print("myfunc() called.")

@lockhelper(mylocker)
@lockhelper(lockerex)
def myfunc2(a, b):
    print("myfunc2() called.")
    return a + b

myfunc()
myfunc2(1, 2)
