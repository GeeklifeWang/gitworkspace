# -*- coding:utf-8 -*-
def fudian(x):
    return float(x)
'''
try:
    x = raw_input('enter:')
    print fudian(x)
except IOError,e:
    print e
except ValueError,e:
    print e


try:
    x = raw_input('enter:')
    print fudian(x)
except (ValueError,IOError):
    print 'Error'


try:
    x = raw_input('enter:')
    print fudian(x)
except (ValueError,IOError),e:
    print e


try:
    x = raw_input('enter:')
except (ValueError,IOError),e:
    print e
else:
    print fudian(x)


try:
    x = raw_input('enter:')
finally:
    x = raw_input('enter:')


try:
    x = raw_input('enter:')
except (ValueError,IOError),e:
    print e
else:
    print fudian(x)
finally:
    x = raw_input('enter:')
'''
#sys exc_info   错误类型
import sys
try:
    print int('a')
except ValueError,e:
    t1=sys.exc_info()
print t1

#traceback format_exc() 错误输出信息
import traceback
try:
    int(a)
except Exception:
    print traceback.format_exc()
