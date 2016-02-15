# -*- coding:utf8 -*-
'函数作为参数传递'
def add_one(x):
    return x+1

def deal(function,seq):
    return [function(i) for i in seq]

myseq = [0,2,4]

'函数指针'
another_del = deal

print another_del(add_one,myseq)

