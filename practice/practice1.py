# -*- coding:utf8 -*-
import os, urllib, re ,traceback

# Find ini file
def resultini(path = r'C:\Program Files (x86)\360\360Safe'):
    result = []
    def recursion(arg = [i for i in os.walk(path)]):
        if isinstance(arg, str):
            if '.ini' in arg:
                #print arg
                result.append(arg)
        elif isinstance(arg, tuple) or isinstance(arg, list):
            for each in arg:
                recursion(each)
        return result
    return recursion.__call__()


# Find url in 360html
def reurl(url = r'http://www.360.cn'):
    try:
        response = urllib.urlopen(url)
        data = response.read()
    except Exception as e:
        print e
        print traceback.format_exc()
    else:
        f = open('360.html', 'w')
        f.write(data)
        f.close()

        string = r'http[s]?://[^\"\"\<\>\=\'\';:]+[\.|\?][a-z]{2,5}'
        l = re.findall(string, data)
        print len(l)
        f = open('result.txt','a')
        for i in l:
            f.write(i + '\n')
        f.close()
