with open('1.txt','r') as f:
    data = f.read(2)
print data

class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"

    def __exit__(self, type,
 value, trace):
        print "In __exit__()"
def get_sample():
    return Sample()
with get_sample() as sample:
    print sample
