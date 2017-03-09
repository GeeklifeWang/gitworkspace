# -*- coding:utf8 -*-
import os, urllib, re

'''Find ini file'''
result = []
path = r'C:\Program Files (x86)\360\360Safe'

def resultgen(path):
    return os.walk(path)

def recursion(arg):
    if isinstance(arg, str):
       if '.ini' in arg:
            #print arg
            result.append(arg)
    elif isinstance(arg, tuple) or isinstance(arg, list):
        for each in arg:
            recursion(each)
    return result
#print recursion([i for i in resultgen(path)])



'''Find url in 360html'''
def reurl(url=r'http://www.360.cn'):
    try:
        response = urllib.urlopen(url)
        data = response.read()
    except Exception as e:
        print e
    else:
        f = open('360.html', 'w')
        f.write(data)
        f.close()

        string = r'http[s]?://[^\"\"\<\>\=\'\';:]+[\.|\?][a-z]{2,5}'
        l = re.findall(string, data)
        print len(l)
        f = open('result.txt','a')
        for i in l:
            f.write(i+'\n')
        f.close()

reurl()
