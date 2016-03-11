#-*- coding:utf8 -*-

def gen():
    for i in range(4):
        print 'gen',i
        yield i
def add(x,y):
    print 'add',x
    print 'result',x+y
    return x+y

g = gen()

#生成器每次绑定n的值，循环三次，最后相当于三个管道连接，n的值为10
for n in [1,5,10]:
    g = (add(n,i) for i in g)
    print list(g)

#这一步生成器开始工作
print list(g)
