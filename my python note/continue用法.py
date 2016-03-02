#-*- coding:utf-8 -*-

#continue用法
#不执行后边的语句，直接开始新的循环
while True:
    A=raw_input('enter:')
    if int(A)==1 :
        print 'keep'
        continue
        break
    else:
        print int(A)

