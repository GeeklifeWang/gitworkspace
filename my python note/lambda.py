def a(n):
    return lambda y:y+n

def b(n):
    return lambda x:x%n

def c(x,n):
    return str(x)+str(n)

#n=1 x=2
print a(1)(2)

#n=2 x=5
print b(2)(5)

#x='a' n='n'
print c('a','b')


d=a(2)
print d(1)


print reduce(lambda x,y:x+y , [x for x in range(10) if x%2 != 0])
