# -*- coding:utf8 -*-

user=raw_input('enter:')
try:
    f=foo()
    #eval()将string转化为名称
    print eval('f.'+user)
    #exec(string,已经打开的文件对象)
    exec('print f.'+user)
except Exception,e:
    print e

