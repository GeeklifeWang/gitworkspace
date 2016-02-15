# -*- coding:utf8 -*-
import itertools as it, glob, os.path
#按类型查找文件 返回文件名和路径
def findfiles(*filetype):
    return it.chain(glob.glob(filetype) for filetype in filetype)
for filelist in findfiles('*.py','*.txt'):
    for eachfile in filelist:
        print eachfile,os.path.realpath(eachfile)
