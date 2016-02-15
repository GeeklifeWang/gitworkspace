from random import randint
from time import sleep
from Queue import Queue
from threading import Thread

def writeq(queue):
    queue.put('xxx', 1)
    print 'write queue, size now %s\n' % queue.qsize()

def readq(queue):
    val = queue.get(1)
    print 'read queue, size now %s\n' % queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeq(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readq(queue)
        sleep(randint(3, 5))

class mythread(Thread):
    def __init__(self, func ,args ,name = ''):
        super(mythread, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def getresult(self):
        return self.result

    def run(self):
        result = apply(self.func, self.args)

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = mythread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'ALL DONE !'

if __name__ == '__main__':
    main()
