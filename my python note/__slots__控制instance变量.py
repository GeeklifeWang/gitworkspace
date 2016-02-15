# -*- coding:utf8 -*-
#类的实例添加变量会报错，类依然可以动态添加变量
class f(object):
    __slots__ = ('version','name')
    def fun(self):
        print self.version

