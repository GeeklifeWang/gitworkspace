# -*- coding:utf8 -*-
class test_del(object):
    '''当类的引用计数(num_count)为0时，就会调用解构器  cmd中查看'''
    num_count = 0
    def __init__(self,name):
        self.__class__.num_count += 1
        self.name=name
        print 'init is running:',self.__class__.num_count
    def __del__(self):
        print 'del running'

A=test_del('1')
B=test_del('2')
C=test_del('3')

#del A,B,C
