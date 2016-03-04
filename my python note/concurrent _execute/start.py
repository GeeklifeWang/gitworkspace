import os
import a,b,c
import threading

import itertools as it, glob

def findfiles(filetype='*.py'):
    return it.chain(glob.glob(filetype))

def myrun(arg):
    return eval(arg+'.run()')

def main():
    filelist = list(findfiles())
    filelist.remove('start.py')
    n = len(filelist)
    threads = []

    print 'start!'

    for each in filelist:
        t = threading.Thread(target=myrun,args=(each[0:-3],))
        threads.append(t)

    for i in range(n):
        threads[i].start()

    for i in range(n):
        threads[i].join()

    print 'done!'

if __name__ == '__main__':
    main()
