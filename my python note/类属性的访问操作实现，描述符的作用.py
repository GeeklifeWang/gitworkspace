# -*- coding:utf8 -*-
x = 1
y = 2

class example(object):
    #定义变量
    A = 1
    B = 'two'
    #定义函数
    def myfunc(self):
        return 'This is my func.'

    def __getattribute__(self, *args, **kwargs):
        print '__getattribute__ is run'
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, attrname):
        print("__getattr__() is run ") 
        return attrname + '    :This my exception deal.'

    def __setattr__(self, attrname, value): 
        print("__setattr__() is run") 
        return object.__setattr__(self, attrname, value)

    def __get__(self, instance ,owner):
        print '__get__() is run'
        return self

class b(object):
    a=example()

'''
python的属性查找策略：对于obj.attr（obj可以是一个类）
1.如果attr是一个Python自动产生的属性，立刻找到。(优先级非常高！)

2.在obj.__class__.__dict__中查找，如果attr存在并且是data descriptor，返回data descriptor的__get__方法的结果，
  如果没有继续在obj.__class__的父类以及祖先类中寻找data descriptor。找不到进行下一步。

3.在obj.__dict__中查找，这一步分两种情况。
  第一种情况是obj是一个普通实例，找到attr就直接返回，找不到进行下一步。
  第二种情况是obj是一个类，依次在obj和它的父类、祖先类的__dict__中查找，
  如果找到一个descriptor就返回descriptor的__get__方法的结果，否则直接返回attr。找不到进行下一步。

4.在obj.__class__.__dict__中查找，如果找到了一个descriptor(这里的descriptor一定是non-data descriptor，如果它是data descriptor，第二步就找到它了)，
  返回descriptor的__get__方法的结果。如果找到一个普通属性，直接返回属性值。找不到进行下一步。

5.Python在这一步，raise AttributeError！
'''
