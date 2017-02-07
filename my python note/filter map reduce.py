# -*- coding:utf8 -*-

'filter(func,iterable) 需要两个参数 第一个为自定义函数 第二个位可迭代的序列 序列中的元素逐一传到自定义函数处理 函数返回为True添加到新的结果列表'

def myfunc1(arg):
    if type(arg) == int:
        return arg
l1 = [11,1,'2','s']
print filter(myfunc1,l1)


'map(func,iterable)    需要两个参数 第一个为自定义函数 第二个位可迭代的序列 序列中的元素逐一传到自定义函数处理 返回的结果添加到新的结果列表'
def myfunc2(arg):
    if type(arg) == int:
        return arg+1

l2 = [1,'2',3]
print map(myfunc2,l2)
print map(lambda x,y:x+y,[1,2,3],[10,10,10])


'''reduce(func,iterable) 需要三个参数 第一个为自定义函数(必须接受两个参数) 第二个位可迭代的序列
第三个为初始值(如果不传迭代序列第一个元素作为初始值)
自定义函数处理的结果作为arg1和迭代序列的下一个元素作为arg2继续执行函数 直到序列迭代完 返回一个最终值'''
def myfunc3(arg1,arg2):
    return arg1.upper()+arg2
l3 = ['a','bc','def']
print reduce(myfunc3,l3)
print reduce(myfunc3,l3,'z')


def str1int(s):
    def fn(x, y):
        print x,y
        return x * 10 + y

    def char1num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char1num, s))
print str1int('123')


