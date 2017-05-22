import Queue

class Stack(object):
    def __init__(self, size=0):
        self.size = size
        self.stack = Queue.LifoQueue(self.size)
    def push(self, arg):
        if not self.stack.full():
            return self.stack.put(arg)
        else:
            print 'stack full'
            return False
    def pop(self):
        if not self.stack.empty():
            return self.stack.get_nowait()
        else:
            print 'stack empty!'
            return False
    def totalsize(self):
        return self.size
    def reverse(self):
        self.temp = Queue.LifoQueue(self.size)
        while not self.stack.empty():
            self.temp.put(self.stack.get_nowait())
        self.stack = self.temp
    def clear(self):
        while not self.stack.empty():
            self.stack.get()
