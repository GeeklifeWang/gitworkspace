#encoding = utf-8

class Person(object):
    population = 0
    list_name = []
    n,m = (0,0)
    
    def __init__(self,name='wang'):
        self.name = name
        Person.list_name.append(name)
        print 'Welcome %s' % self.name
        Person.n += 1
        Person.m += 1
        Person.population += 1

    def __del__(self):
        print '%s is died' % self.name

        for i in range(Person.n):
            if Person.list_name[i] == self.name:
                Person.list_name[i] = ''
        Person.m -= 1
        Person.population -= 1

        if Person.population == 0:
            print 'Nobody.'
        else:
            print 'There still have %d people alive.' % Person.population
        print Person.list_name,

    def Hi(self):
        print 'Hi,my name is %s' % self.name

    def Howmany(self):
        if Person.population == 1:
            print 'only one people'
        else:
            print 'have %d people' % Person.population
        print Person.list_name
