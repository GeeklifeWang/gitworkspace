# -*- coding:utf8 -*-

class father(object):
    _age = 42
    def __init__(self,name):
        self.name = name
        print self.name    
    def printf(self):
        print 'father class'

class son1(father):
    def printf(self):
        super(son1,self).printf()
        print 'son1 class'

class son2(father):
    def __init__(self,name):
        super(son2,self).__init__(name)
        #father.__init__(self,name)
    def printf(self):
        print 'son2 class'

#新式类的mro遵循广度搜索，先找兄弟类，父类   旧式类的mro遵循深度遍历  p385
father.__mro__

#判断cls1是否是cls2的子类   cls2可以是类元组
def panduan(cls1,cls2):
    return issubclass(cls1,cls2)
#判断arg1是否为arg2的实例  arg2可以是元组
isinstance(0.1,float)
