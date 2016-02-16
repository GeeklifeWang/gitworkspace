#-*- coding:utf-8 -*-
'''
splinter和之后的selenium可能因版本差异导致无法调用chromedriver服务，修改
selenium\webdriver\common\service.py中，Service类初始化操作中的self.path参数
execuable传的参数为chromedriver，非chromedriver的路径，手动复制self.path为
chromedriver的本地路径，即可修复此问题.
'''
#import os
#from selenium import webdriver
from splinter.browser import Browser
import time

#driver = webdriver.Chrome('D:\\Chrome31\\chromedriver.exe')
#os.environ['webdriver.chrome.driver'] = 'D:\\Chrome31\\chromedriver'

browser = Browser('chrome')

testUrl = 'http://www.baidu.com'

def test():
    browser.visit(testUrl)

    browser.find_by_id('kw').fill(u'刘浩博')
    time.sleep(2)
    browser.find_by_value(u'百度一下').first.click()
    time.sleep(5)
    
    browser.quit()
    print 'done'

test()
