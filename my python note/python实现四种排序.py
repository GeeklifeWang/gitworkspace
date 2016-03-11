# -*- coding:utf8 -*-

l = [23,4,11,7,9,50]
n = len(l)

#冒泡
def bubble_sort(arg=l):
    for i in range(0,n):
        for j in range(i,n):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
    return l

#选择
def select_sort(arg=l):
    for i in range(0,n):
        mindex = i
        for j in range(i,n):
            if l[mindex]>l[j]:
                mindex = j
        l[mindex],l[i] = l[i],l[mindex]
    return l

#插入
def insert_sort(arg=l):
    for i in range(1,n):  
        tmp = l[i]  
        j = i  
        while(j>= 1):
            if tmp<l[j-1]:
                l[j] = l[j-1]
                j = j-1 
            else:  
                break    
        l[j] = tmp  
    return l  

#快排
def quick_sort(arg=l): 
    n=len(arg)
    if n<=1:
         return arg
    right= []
    left = []
    p = arg.pop(n/2)
    for item in arg:
        if item < p:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left)+[p]+quick_sort(right)


print bubble_sort()
print select_sort()
print insert_sort()
print quick_sort()
