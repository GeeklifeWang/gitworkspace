# -*- coding:utf8 -*-
#通过__getattr__动态返回路径, 找不到的路径, F初始化动态修改self.path, 然后__str__返回

'''
class F(object):
    def __init__(self, path):
        self.path = path
    def __getattr__(self,path):
        return F('%s/%s' % (self.path, path))
    def __str__(self):
        return self.path
    __repr__ = __str__

f=F('user')
print f.bin.env

'''
class F(object):
    def __init__(self, path, val):
        if val:
            self.path = path+r'/'+val
        else:
            self.path = path
            
    def __getattr__(self,path,val=''):

        return F(r'%s/%s' % (self.path, path), val)
    
    def __str__(self):
        return self.path
    __repr__ = __str__

    def __call__(self,*args):
        l=[]
        for i in args:
            l.append(str(i))
        return self.path + '/' + ('/'.join(l))


f=F('user','wang')
#print f(123,456,'a')

print f.a.b
