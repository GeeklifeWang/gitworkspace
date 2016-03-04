# -*- coding:utf8 -*-
import unittest

class Method(object):
    def value(self):
        return 'value'
    def setvalue(self,val):
        return val

#覆盖setUp和tearDown，编写testcase
class TestMethodCase(unittest.TestCase):
    def setUp(self):
        self.method = Method()
        #print 'set'
    def tearDown(self):
        self.method = None
        #print 'tear'
    def test_value(self):
        self.assertEqual(self.method.value(), 'value')
    def test_setvalue(self):
        self.testvalue = 'new'
        self.assertEqual(self.method.setvalue(self.testvalue), self.testvalue )

#仅覆盖runTest测试一条testcase,若正确，则无输出，否则引起AssertionError
class runTestMethodCase(unittest.TestCase):
    def runTest(self):
        self.testvalue = 'run_new'
        method = Method()
        self.assertEqual(method.setvalue(self.testvalue), self.testvalue) #,123)

def suite():

    #normal
    suite = unittest.TestSuite()
    suite.addTest(TestMethodCase('test_value'))
    suite.addTest(TestMethodCase('test_setvalue'))

    #use map
    #map(suite.addTest,(TestMethodCase('test_value'),TestMethodCase('test_setvalue')))

    #if all testcase start with test
    #suite = unittest.makeSuite(TestMethodCase,'test')

    return suite

    '''
    #or moer testsuite
    alltestsuite = unittest.TestSuite(suite1,suite2)
    return alltestsuite
    '''

if __name__ == '__main__':
    #normal
    unittest.main(defaultTest = 'suite')

    #if all testcase start with test
    unittest.main()

    #another way to do
    #runner = unittest.TextTestRunner()
    #runner.run(suite())

    #覆盖runTest测试
    #do = runTestMethodCase()
    #do.runTest()
