import threading
import time

loops = [2,5]

def loop(nloop,sleeptime):
    print 'start loop %d at:%s\n' % (nloop, time.ctime())
    time.sleep(sleeptime)
    print 'loop %d done at:%s\n' % (nloop, time.ctime())

def main():
    print 'starting at:', time.ctime()
    threads = []
    nloops= range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        #不要用run,用start启动
        'start是起一个新的线程执行方法'
        threads[i].start()
        'run是在当前线程执行方法'
        #threads[i].run()

    for i in nloops:
        threads[i].join()

    print 'all done at:', time.ctime()

if __name__ == '__main__':
    main()
