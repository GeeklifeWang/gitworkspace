class xingming(object):
    def __init__(self, name):
        self.name = name
    def tell(self):
        print 'my name is %s' % self.name

class xueke(xingming):
    def __init__(self, major):
        super(student,self).__init__()
        self.major = major
    def tell(self):
        print 'my najor is %s' % self.major

class nianling(xueke):
    def __init__(self, age):
        super(student,self).__init__()
        self.age = age
    def tell(self):
        print "I'm %d years old" % self.age       

'''
class student(nianling):
    def __init__(self,sex):
        super(student,self).__init__()
        self.sex = sex
    def tell(self):
        xingming.tell(self)
        xueke.tell(self)
        nianling.tell(self)
        print "sex: %s" % self.sex

'''
class xingming(object):
    def __init__(self, name):
        self.name = name
    def tell(self):
        print 'my name is %s' % self.name

class xueke(object):
    def __init__(self, major):
        self.major = major
    def tell(self):
        print 'my najor is %s' % self.major

class nianling(object):
    def __init__(self, age):
        self.age = age
    def tell(self):
        print "I'm %d years old" % self.age  

class student(xingming, xueke,nianling):
    def __init__(self, name, major, age, sex):
        xingming.__init__(self,name)
        xueke.__init__(self,major)
        nianling.__init__(self,age)
        self.sex = sex
    def tell(self):
        xingming.tell(self)
        xueke.tell(self)
        nianling.tell(self)
        print "sex: %s" % self.sex

wo = student('wang','computer',22,'boy')
