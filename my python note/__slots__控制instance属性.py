# -*- coding:utf8 -*-
#类的实例添加属性会报错，类依然可以动态添加属性（方法和变量）
#类本身拥有的属性不受slots限制,实例可以用，并且实时更新
class F(object):
    __slots__ = ('c')
    def a(self):
        print 'aaa'
    def b(self):
        print 'bbb'

f = F()
