# -*- coding:utf8 -*-
#必须在cmd命令行中才能执行  python+文件名  可以看到输出
import os,time,sys
from multiprocessing import Process

# 子进程要执行的代码
def run_proc():
    print time.ctime()
    print 'Run child process (%s)...' % os.getpid()


if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc)

    print 'Process will start.'
    p.start()
    print p.is_alive()
    p.join()
    print 'Process end.'
