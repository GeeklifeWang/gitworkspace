# -* coding:UTF-8 *-

class A():
    distance = raw_input("distance:")
    totalTime = raw_input("totalTime:")
    def velocity(self):
        self.distance = A.distance
        self.totalTime = A.totalTime
        rate = int(self.distance) / int(self.totalTime)
        print float(rate)
a=A()
a.velocity()



a=raw_input('enter:')
b=raw_input('enter:')
def cheng(a,b):
    return (int(a)*int(b))
print cheng(a,b)


import random
list1 = []
Value = round(random.random() , 2)
tuple1 = (Value,)
value = tuple1[0]
print "money is:" , Value
for i in range(100):
    for i in (0.25 , 0.10 , 0.05 , 0.01):
        while True:
            shang = Value // i
            yu = Value % i
            list1.append(shang)
            list1.append(yu)
            break
        Value = yu
#print "25meifen:%d" % int(list1[0])
#print "10meifen:%d" % int(list1[2])
#print "5meifen:%d" % int(list1[4])
#print "1meifen:%d" % int(list1[6]+1)
#print list1
    prove = int(list1[0])*0.25 + int(list1[2])*0.10 + \
    int(list1[4])*0.05 + int(list1[6]+1)*0.01
    if prove == value:
        print 'Yes'
    else:
        print 'No'
        print prove,value

#控制程序执行时间
import time
print 1
time.sleep(10)#等待10s
print "start"
