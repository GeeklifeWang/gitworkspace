#-*- coding:utf8 -*-
#locals()和globals()

a = 1
b = 2
#当前的locals实际上就是全局的globals
print locals()
print globals()

def func():
    a = 3
    #局部的locals不包含全局变量
    print locals()
    d = 4
    #局部变量的增加、修改不影响全局变量
    print globals()
    #第一次打印局部变量时，没有定义d，
    print locals()

func() 
    
