def foo(arg1, arg2, *arg, **kwarg):
    print arg1
    print arg2
    print arg
    print kwarg

t = (1,2,3)
d = {'a':11,'b':22,'c':33}


foo('arg2','arg1',1,2,a=11,b=22,c=33)
print
foo('arg1','arg2',*t,**d)

