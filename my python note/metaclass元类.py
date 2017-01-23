#-*- coding:utf8 -*-

#通过type创建类
#classname = type(clsname,base,attrdict)

#经典类无法使用元类继承
class Father(object):
    def __init__(self):
        self.age = 40
        self.name = 'wang'
        self.t = 20170123
    def printage(self):
        age = self.age
        print age
    def printname(self):
        name = self.name
        print name
    def printtime(self):
        t = self.t
        print t

def classcontrol(cls,base,attr):
    #print 'cls:',cls
    #print 'base:',base
    #print 'attr:',attr
    return type(cls, base+(Father,), attr)

#class Son(Father):
class Son1():
    __metaclass__ = classcontrol
    def __init__(self):
        super(Son1, self).__init__() #新式类继承init
        #Father.__init__(self) #经典类继承init
        self.age = 20
        self.id = 'student'

    def printid(self):
        i = self.id
        print i
        
#调用
s = Son1()
s.printtime()
s.printage()
s.printid()

print'#'*15

#把作用域中非buildin方法名大写
class UpperAttrMetaclass(type):
    #用__new__方法创造类，在__init__之前工作
    def __new__(cls, name, base, dct):
        #print dct
        #寻找非__开头的方法改成大写
        for k,v in dct.items():
            if not k.startswith('__'):
                dct[k.upper()] = v
                del dct[k]
        #返回的类的base继承添加Father类
        #return type.__new__(cls, name, bases, dct)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, base, dct)

class Son2(Father):
    __metaclass__ = UpperAttrMetaclass
    def __init__(self):
        super(Son2, self).__init__() #新式类继承init
        #Father.__init__(self) #经典类继承init
        self.age = 25
        self.id = 'worker'

    def printid(self):
        i = self.id
        print i

#调用
b = Son2()
b.printtime()
b.printage()
b.PRINTID()
