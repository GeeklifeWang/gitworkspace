# -* coding:UTF-8 *-

print 'I \'m \"wang\"'  # \ 对标点进行转译
print r'I \'m \"wang\"' # r 后的语句不转译

#排序
a = [0,1,4,3,9,5,12,7,8,9]
b = ['b','z','a','abcd','adc','aa',]
#将list a中元素倒序列保存
a.reverse()
#将list a中元素按从小到大排序（默认）
a.sort(reverse = False)
#将list a中元素按从大到小排序
a.sort(reverse = True)
#将list b中元素按字符串长度排序
def listsort(newlist):
    dictb = {}
    dictB = []
    for i in range(len(newlist)):
        #dictb.[b[i]] = len(b[i])
        dictb.setdefault(newlist[i], len(newlist[i]))

    #'[0]按key [1]按value Ture升序 False降序 不改变原字典 dictB是列表'
    dictB = sorted(dictb.iteritems(), key = lambda asd:asd[1], reverse = False)
    for i in range(len(dictB)):
        newlist[i] = (dictB[i][0])   
    print newlist

#切片操作
print a
print a[:]     #从头到尾
print a[::]    #从头到尾按1
print a[5::-1] #从5到头按-1
print a[:5:-1] #从尾到5按-1
print a[::-1]  #从尾到头按-1

#列表连接
a = [1,2,3,4,5]
b = [1,2,0]
print 0 in a #判断”0“是否在列表a中
a += b
print a
print 0 in a

#extend和append的区别
a.extend(b)
print a
a.append(b)
print a


# 可以跨行显示
a = raw_input('''
1.烤肉
2.火锅
3.西餐
please enter choice: ''')
if a != '':
    print '不给你！哈哈！'
else:
    pass


import operator
"索引 None+range()"
a = [1,2,3]
b = a * 2

i = -1
for i in [None] + range(-1, -len(b), -1):
    print b[:i]
#求和    
print sum(b)
print reduce(operator.add, b)
#最大最小值
print max(a)
print min(a)


'返回list整除index的value'
num_str = raw_input('enter a number:')
num_num = int(num_str)
fac_list = range(1,num_num+1)
print fac_list
l1 = fac_list[:]
for i in l1:
    if (num_num % i == 0):
        del fac_list[fac_list.index(i)]


#类和函数的调用
class MyClass(object):
	version=0.1
	def __init__(self,nm='wang'):
		self.name=nm
		print 'init print is',nm
	def showname(self):
		print 'your name is',self.name
		print 'My name is',self.__class__.__name__
	def showver(self):
		print self.version
	def addMe2Me(self,x):
		return x+x


#循环count %的使用
a=0
b=0
for i in range(5):
    b=raw_input('enter No.%d number:' % (i+1))
    a+=int(b)
print a

#__doc__应用
x=1
y=2
def a(x,y):
    'This is print big value'
    if x>y:
        print x
    else:
        print y
a.__doc__

#读取txt文本每行
fobj=open(filename,'r')
for eachLine in fobj:
    print eachLine,
fobj.close()

#写入txt文本
filename=raw_input('enter name:')
fobj=open(filename,'w')
for i in range(5):
    print >> fobj,'%d' % i
fobj.close()

#pass用法
a=''
a=raw_input('SA:')
if a=='wangyouwei':
    pass
elif a=='liuhaobo':
    print '%s is big SB!' % (a)

#两值互换
x,y=1,2
x,y=y,x
print x,y

#while循环
def No():
    print 'no'
def Yes():
    print 'yes'

while(True):
    A=raw_input('enter value:')
    if int(A)>10:
        Yes()
        break
    else:
        No()

#字符串空格处理
"   xyz   ".strip()            # returns "xyz"  
"   xyz   ".lstrip()           # returns "xyz   "  
"   xyz   ".rstrip()           # returns "   xyz"  
"  x y z  ".replace(' ', '')   # returns "xyz" 
