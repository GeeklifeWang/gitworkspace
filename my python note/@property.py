#-*- coding:utf8 -*-

'''property的作用是将 类方法 转换成 类属性 直接访问'''
'''
class f(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score_set(self, value):
        self._score = value
    @score.deleter
    def score_del(self):
       del self._score
'''
'''
class c(object):
    def __init__(self,val):
        self._x = val
    @property
    def fget(self):
        return self._x
    @fget.setter
    def fset(self, val):
        self._x = val
    @fget.deleter
    def fdel(self):
        del self
'''
class classproperty(object):
    def __init__(self,func):
        self.func = func
    def __get__(self,instance,cls):
        print instance
        return self.func(cls)
class Father(object):
    @classproperty
    def name(cls):
        return cls.__name__.lower()
class kid(Father):
    pass


