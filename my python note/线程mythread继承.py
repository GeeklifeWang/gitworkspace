import threading
import time

class mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.result

    def run(self):
        #print '%s  run   at: %s\n' % (self.name,time.ctime())
        self.result = apply(self.func,self.args)
        #print '%s finish  at: %s\n' % (self.name,time.ctime())

loops = [2,4]

def loop(nloop,sleeptime):
    print 'start loop %d at:%s\n' % (nloop, time.ctime())
    time.sleep(sleeptime)
    print 'stop  loop %d at:%s\n' % (nloop, time.ctime())
    return 'success'

def main():
    print 'start at:%s\n' % time.ctime()
    threads = []
    nloops= range(len(loops))

    for i in nloops:
        t = mythread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        #threads[i].setDaemon(True)
        threads[i].start()
        threads[i].run()
        print threads[i].getResult()
       
    for i in nloops:
        threads[i].join() 

    print 'all done at:', time.ctime()

if __name__ == '__main__':
    main()
