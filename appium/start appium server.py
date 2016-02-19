#-*- coding:utf8 -*-
import os
import threading
import time

#端口不冲突，就可以启动多个appium服务，对应多个脚本，执行多台设备的测试
#os.system('appium -a127.0.0.1 -p4723 -U05157df510243104')
#os.system('appium -a127.0.0.1 -p4725 -UP4M0215216007050 --no-reset')
#os.system(r'monkeyrunner.bat C:\Users\youwei\Desktop\monkeyrunnerTest.py')


def main():
    n = 2
    print 'starting at:', time.ctime()
    threads = []
    argument_list = ['appium -a127.0.0.1 -p4723 -U05157df510243104'
                     ,'appium -a127.0.0.1 -p4725 -UP4M0215216007050']

    for i in range(n):
        t = threading.Thread(target=os.system,args=(argument_list[i],))
        threads.append(t)

    for i in range(n):
        threads[i].start()

    for i in range(n):
        threads[i].join()

    print 'all start at:', time.ctime()

if __name__ == '__main__':
    main()
