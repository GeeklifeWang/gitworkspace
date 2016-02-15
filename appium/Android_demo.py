# -*- coding:utf8 -*-
from appium import webdriver
import time
#import os
#import unittest

#PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def startapp():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    #desired_caps['deviceName'] = '4df727dd1300bf99'#三星s3
    desired_caps['deviceName'] ='P4M0215216007050'#华为mate7
    desired_caps['appPackage'] = 'com.moji.mjweather'
    desired_caps['appActivity'] = 'com.moji.mjweather.activity.main.MainActivity'
    #desired_caps['app']= PATH('C:\\Users\\youwei\\Desktop\\MJWeather_5.8.6-release-sign.apk')
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboaed'] = 'True'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    time.sleep(2)

    driver.swipe(540,1200,540,400)

    driver.find_element_by_name(u"时景").click()
    driver.find_element_by_name(u"我").click()

    #driver.find_element_by_id('id').send_keys('string')

    #element_list = driver.find_elements_by_class_name('android.xxxx')
    #element_list[n].click()

    driver.quit()

if __name__ == '__main__':
    try:
        startapp()
    except Exception, e:
        print e
    else:
        print 'done!'

