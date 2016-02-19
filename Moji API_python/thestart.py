#-*- coding:utf-8 -*-

import os
import itertools as it
import glob
import time


def mytest():
    #查找路径下所有文件，去掉执行脚本
    allfile = os.listdir('C:\\Users\\youwei\\Desktop\\Moji API_python')
    allfile.remove('thestart.py')
    allfile.remove('thefail.py')
    #定义日志输入文件
    resultfile='log.txt'
    while True:
        if os.path.exists(resultfile):
            print 'WARNING: %s already exists!\n' % resultfile
            choose = raw_input('Do you want to overwrite this file? (y/n):')
            if choose == 'y':
                break
            elif choose == 'n':
                resultfile = raw_input('Please enter a new file name:') + '.txt'
                break   
        else:
            break

    #查找所有txt文件，并去掉
    def findfiles(filetype):
        return it.chain(glob.glob(filetype))
    for eachtxt in findfiles('*.txt'):
        allfile.remove(eachtxt)

    #逐一执行脚本，并输出日志
    os.popen('cd Desktop\\Moji API_python')

    f = open(resultfile,'a')
    f.write(time.ctime()+'\n')

    '''
    for each in allfile:
        try:
            #os.popen('python'+' '+each)
        except Exception,e:
            f.write(each+' '+'fail'+':'+e+'\n')
        else:
            f.write(each+' '+'success'+'\n')
    '''
    for each in allfile:
        output = os.popen('python'+' '+each)
        #print output.read()
        if output.read():
            f.write(each+' '+'success'+'\n')
        else:
            f.write(each+' '+'fail'+'\n')

    f.close()
    print 'finish!'


if __name__ == '__main__':
    mytest()
