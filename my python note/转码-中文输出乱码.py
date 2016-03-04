# -*- coding:utf-8 -*-
'''
os.walk(top, topdown=True, onerror=None, followlinks=False) 
可以得到一个三元tupple(dirpath, dirnames, filenames),
第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件
dirpath 是一个string，代表目录的路径
dirnames 是一个list，包含了dirpath下所有子目录的名字
filenames 是一个list，包含了非目录文件的名字
这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name)
'''
import os
'''
filedir = "C:\\Users\\youwei\\Desktop\\墨迹天气\\考勤".decode('utf8').encode('gbk')
for a,b,c in os.walk(filedir):
    print a
    print b
    for i in c:
        print i
'''
#print '%d字节'.decode('utf8').encode('gbk') % os.path.getsize('C:\\Users\\youwei\\Desktop\\1.txt')

#print '%d字节'.decode('utf8').encode('gbk') % os.path.getsize("C:\\Users\\youwei\\Desktop\\墨迹天气\\考勤\\1.txt".decode('utf8').encode('gbk'))
print '%d字节' % os.path.getsize("C:\\Users\\youwei\\Desktop\\墨迹天气\\考勤\\1.txt")
