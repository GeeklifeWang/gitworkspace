#-*- coding:utf8 -*-

x = 1

def bar():
    x = 2
    print x
    def foo():
        y = 1
        print  x+y
    foo()

bar()

print x

class f():
    global x
    x=3
    def __init__(self):
        print x

F=f()

print x
