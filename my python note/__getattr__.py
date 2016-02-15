# -*- coding:utf8 -*-
class a(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self,attr):
        return getattr(self,attr)

A=a('wang')
#用 getattr(类,属性,未找到属性输出)来确定类中是否有该属性
print A.__getattr__('name')
