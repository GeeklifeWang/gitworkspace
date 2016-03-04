# encoding=utf-8
import threading
import time
 
class ThreadImpl(threading.Thread):
  def __init__(self, num):
    threading.Thread.__init__(self)
    self._num = num
  def run(self):
    global total, mutex
 
    for x in xrange(0, int(self._num)):
      # 取得锁
      mutex.acquire()
    
      total = total + 1

      # 打印线程名
      print threading.currentThread().getName()
      print total
      print time.ctime()

      # 释放锁
      mutex.release()
 
if __name__ == '__main__':
  #定义全局变量
  global total, mutex
  total = 0
  # 创建锁
  mutex = threading.Lock()
  
  #定义线程池
  threads = []
  # 创建线程对象
  for x in xrange(0, 2):
    threads.append(ThreadImpl(5))
  # 启动线程
  for t in threads:
    t.start()
  # 等待子线程结束
  for t in threads:
    t.join()  

#不加线程锁的时候，线程池里的两个线程并行操作（一起打印total，aaa）
#加线程锁的时候，线程池里的两个线程并发操作（第一个打印total，aaa 然后第二个再来）
#多线程是共享资源的，使用的是全局变量
#加锁的资源，使用完资源必须要将这个锁打开，让其他线程使用
