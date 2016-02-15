# -*- coding:utf8 -*-
#只有类内部覆盖了__call__时，才可以使用实例()
class foo(object):
    def __call__(self,*args):
        print 'cal1:',args
    def p2(self):
        print 'p2 done.'

f=foo()
f.p2()
f(1,2,3)
