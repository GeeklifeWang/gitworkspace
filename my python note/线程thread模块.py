#-*- coding:utf-8 -*-

'''thread模块使用实例'''

import thread, time

loops = [4,2]

def loop(nloop,sleeptime,lock):
    print 'start loop %d at %s\n' % (nloop, time.ctime())
    time.sleep(sleeptime)
    print 'loop %d done at:%s\n' % (nloop, time.ctime())
    lock.release()

def main():
    print 'starting at:', time.ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock =thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all done at:', time.ctime()

if __name__ == '__main__':
    main()
