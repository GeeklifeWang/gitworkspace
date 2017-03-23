# -*- coding:utf8 -*-
import threading

class Thread_Count(object):
    def __init__(self, n):
        self.n = n
        self.result = 0
        self.number = []
        self.threadlist = []
        self.mutex = threading.Lock()

    def counter(self, arg):
        r = sum(arg)
        self.mutex.acquire()
        self.result += r
        self.mutex.release()

    def split_list(self):
        if self.n >= 100:
            self.n = 100
            self.number = [[x] for x in xrange(1, 101)]
        else:
            for i in range(1, self.n + 1):
                if (i-1) == 0:
                    l = range((i-1)*(100/self.n) + 1, 100*i/self.n + 1)
                else:
                    l = range((i-1)*(100/self.n) + 1, (i-1)*(100/self.n) + 1 + 100/self.n)
                    if i == self.n:
                        last = range((i-1)*(100/self.n) + 1 + 100/self.n, 101)
                        #l.extend(range((i-1)*(100/self.n) + 1 + 100/self.n, 101))
                self.number.append(l)
            for j in self.number:
                try:
                    j.append(last.pop())
                except Exception as e:
                    break
        return self.number

    def thread_do(self):
        for i in xrange(len(self.number)):
            t = threading.Thread(target = self.counter, args = (self.number[i],) )
            self.threadlist.append(t)
        for t in self.threadlist:
            t.start()
        for t in self.threadlist:
            t.join()

if __name__ == "__main__":
    while True:
        a = raw_input('please enter "n" value: ')
        mycount = Thread_Count(int(a))
        mycount.split_list()
        mycount.thread_do()
        print mycount.result
