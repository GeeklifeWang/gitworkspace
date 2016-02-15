j, k = 1, 2
def p1():
    j, k = 3, 4
    print 'j = %d, k = %d' % (j, k)
    k = 5
    print 'j = %d, k = %d' % (j, k)
def p2():
    j = 6
    p1()
    print 'j = %d, k = %d' % (j, k)

p1()
p2()
k = 7
print 'j = %d, k = %d' % (j, k)
