# -*- coding:utf-8 -*-
#自定义
import traceback
class LengthRequiredException(Exception):
    def __init__(self,length,minLength):
        Exception.__init__(self)
        self.length = length
        self.minLength = minLength

l = [0,1,2,3]
minLength = 5
try:
    if len(l) != minLength:
        raise LengthRequiredException(len(l),minLength)
    else:
        pass

#except LengthRequiredException:
#    print("Length not fit :length is %d required %d" %(LengthRequiredException(len(l),minLength).length,LengthRequiredException(len(l),minLength).minLength))

except LengthRequiredException as e:
    print("Length not fit :length is %d required %d" %(e.length,e.minLength))
else:
    print("no exception was raised")
finally:
    print("finally over")

#raise
#raise Exception,'raise'
