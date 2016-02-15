# -*- coding:UTF-8 -*-
"py调用adb获取moji内存   adb nodaemon server 查adb端口"

import time
import os
from pyadb.adb import ADB
from pyExcelerator import *

n = 3      #循环次数
list1 = [] #第一次ADB.output的数据 写入txt
list2 = [] #从txt读取的数据
list3 = [] #处理从txt读取的数据
a = 0      #内存行数
b = 0      #内存列数

fname = '%s.txt' % raw_input('enter file name:')
if os.path.exists(fname):
        print ('ERROR: %s already exists\n' % fname)
        quit()

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')

#myadb.restart_server()      '重启adb服务'
#print myadb.get_logcat("I") '打印log'

for i in range(n):
    print myadb.get_devices()
    #myadb.shell_command("dumpsys meminfo com.moji.mjweather")
    myadb.shell_command("dumpsys meminfo com.moji.wallpaper")

    "写入txt"
    list1.append('NO.%d   TIME    GET  MOJI  MEMORTDATA:\n' % (i+1))
    list1 += myadb.get_output()
    list1.append('      \n')
    fobj = open(fname,'w')
    fobj.writelines(['%s' % (x) for x in list1])
    fobj.close()
    if i < (n-1):
            time.sleep(120)    #等待1s

fr = open('%s' % fname, 'r')
list2 = fr.readlines()
for g in range(len(list2)):
        list2[g] = list2[g].strip('\r\r\n')#list2去掉\r\r\n
        if list2[g] != '' and list2[g] != ' ':
                list3.append(list2[g])#写入list3
        else:
                pass
print list3
'写入Excel'
writejob = Workbook()                   #创建一个工作簿
newsheet1 = writejob.add_sheet('all')   #创建一个工作表
newsheet2 = writejob.add_sheet('total') #创建一个工作表
for k in range(len(list3)):
        newsheet1.write(k, 0, list3[k])
        writejob.save('memoryinfor_data.xls')

'处理total内存'
for j in range(len(list3)):
        strj = ''
        str1j = ''
        strj = ''.join(list3[j])
        strj = strj.strip()
        #print "strj:%s" % strj
        #strj = strj.replace(' ' , '')

        for k in range(len(strj)):
                if strj[k].isspace():
                        str1j = strj[:k]
                        strj = strj[k:]
                        #print str1j
                        #print strj
                        break

        if (str1j == 'TOTAL'):
                for m in range(len(strj)):
                        if not strj[m].isspace():
                                strj = strj[m:]
                                break

        for n in range(len(strj)):
                if strj[n].isspace():
                        str1j = strj[:n]
                        strj = strj[n:]
                        #print "str1j:%s" % str1j
                        #print "strj:%s" % strj
                        break

        if str1j.isalnum():
                newsheet2.write(a, 0, str1j+' KB')
                #newsheet2.write(a, 0, str(round(((int(str1j)/1024)),3))+'MB')
                writejob.save('memoryinfor_data.xls')
                print str1j
                print 'input!'
                a += 1
                b += 1

fr.close()
print 'done!'
