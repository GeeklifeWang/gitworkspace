# -*- coding:utf8 -*-

class A:#(object):
    def printf(self):
    	print 'A'

class B(A):
	pass

class C(A):
	def printf(self):
		print 'C'

class D(B,C):
	pass

d = D()
d.printf()


'经典类输出：A'
'新式类输出：C'


'经典类是深度优先搜索，先查找左侧树（父类B，祖先类A），再查找右侧树（父类C，祖先类A）' #B中没有printf方法，A中有，所以执行A的printf
'新式类是广度优先搜索，先查找父类（兄弟类B，C），先左后右，再寻找上一层（祖先类A）'    #B中没有printf方法，C中有，所以执行C的printf