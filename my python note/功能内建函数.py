#encoding=utf-8
#功能函数
'''
'返回a绝对值'
abs(a)

'返回一个元组（两个元素）'
coerce(a,b)

"返回a/b的商和余"
divmod(a,b)

"a的b次方"
pow(a,b)

"把a四舍五入  b为精确到小数点后几位"
round(a,b)

"返回number的16进制"
hex(number)

"返回number的8进制"
oct(number)

"返回字符的ASCII码"
ord('a')

"返回 int 的字符值"
chr(int)

unichr(int)
'''
'''
#列表解析
str1 = ['abc','ijk','xyz']

str2 = 'abc'
list1 = []

print [ord(i) for i in str2]
print [[row[i] for row in str1] for i in range(3)]
for i in range(3):
    print i
    for row in str1:
        print row,row[i]
        list1.append(row[i])
        print list1

str1 = 'abc'
str2 = 'lmn'
list1 = []
list2 = []
list3 = [1,2,3]
print cmp(str1,str2)
for i in str1:
    list1.append(ord(i))
for j in str2:
    list2.append(ord(j))
print sum(list3)
print sum(list1)-sum(list2)
'''
#enumerate 和 zip
a = 'happy'
b = 'day'
for i,char in enumerate(a):
    print i,char
print zip(a,b)
