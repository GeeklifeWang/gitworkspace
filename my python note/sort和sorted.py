#-*- coding:utf8 -*-

#list.sort(cmp=None,key=None,reverse=False)
'sort是list的成员函数，会改变原有list顺序，'
#sorted(iterable,cmp=None,key=None,reverse=False)
'sorted是buildin函数，需要传入数据，不改变原输入，返回新结果'

'iterable:可迭代的对象'
'cmp:比较函数逻辑'
'key:比较元素对象'
'reverse:False=升序|True=降序'

    
l = [5,4,3,2,1,6]
print 'l:',l
l.sort(reverse=False)
print 'up:',l
l.sort(reverse=True)
print 'down:',l


d = {'a':4,'d':5,'c':3,'b':2}
print sorted(d.items(), key=lambda x:x[1])
print sorted(d.items(), key=lambda x:x[0])
