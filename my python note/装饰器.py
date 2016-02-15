
from time import sleep,ctime
def fun_decorate(function):
    def print_time_fun():
        print '[%s] %s is called' % (ctime(),function.__name__)
        return function
    return print_time_fun
@fun_decorate
def foo():
    print 'fffff'
def main():
    for i in range(3):
        foo()
        sleep(5)

if __name__ == '__main__':
    main()


