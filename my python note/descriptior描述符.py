#coding=utf-8
class A(object):
    def __init__(self):
        self.attr = 10
    def __get__(self, obj ,owner):
        print '__get__() is run'
        print 'obj:',obj
        print 'owner:',owner
        return self.attr

    def __set__(self,obj,val):
        print '__set__() is run'
        print 'obj:',obj
        print 'val:',val
        self.attr = val

    def __delete__(self,obj):
        print '__del() is run__'
        print 'obj:',obj
        del self.attr

class B(object):
    a=A()
    
    s1 = 1
    s2 = 'two'
    
    def c(self):
        return 'This is my func.'

    def __getattribute__(self, *args, **kwargs):
        print '__getattribute__ is run'
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, attrname):
        print("__getattr__() is run ") 
        return attrname + ':This my exception deal.'
        #__getattribute__找不到属性后会调用__getattr__并报出异常AttributeError
        #return object.__getattr__(self, attrname)

    def __setattr__(self, attrname, value): 
        print("__setattr__() is run") 
        return object.__setattr__(self, attrname, value)

    def __delattr__(self, attrname): 
        print("__delattr__() is run") 
        return object.__delattr__(self, attrname)
    
b = B()
