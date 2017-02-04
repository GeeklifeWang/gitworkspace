#coding:utf-8
class test_del(object):
    '''当程序退出时  python解释器会调用解构器清除实例对象  cmd中查看'''
    num_count = 0
    def __init__(self,name):
        self.__class__.num_count += 1
        self.name=name
        print self.name,':',self.__class__.num_count
    def __del__(self):
    	self.__class__.num_count -= 1
    	print 'del running'
    	print self.name,':',self.__class__.num_count
    
A=test_del('a')
B=test_del('b')
C=test_del('c')
