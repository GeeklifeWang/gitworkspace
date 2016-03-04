# -*- coding:utf8 -*-
class AccessCounter(object):
    
    def __init__(self, value):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('money', value)

    def __setattr__(self, attr, value):
        #计算money属性的访问次数
        if attr == 'money':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)

        #调用父类object的__setattr__进行赋值操作
        #super()用于继承父类属性，只能用于新式类，等同于object.__setattr__(self,attr,value)
        super(AccessCounter, self).__setattr__(attr, value)
       
        #慎重！！如果使用self.name = val，则会调用当前类修改后的__setattr__，
        #从而继续执行self.name=value，导致程序陷入无穷递归并报错 

    #同__setattr__
    def __delattr__(self, attr):
        if attr == 'money':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(attr)


    #当找不到某属性时会调用，（与赋值操作区分开）
    def __getattr__(self,attr):
        return 'undefine'

a = AccessCounter(1)
