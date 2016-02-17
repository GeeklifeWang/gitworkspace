#-*- coding:utf8 -*-

import os
import time
from pyadb.adb import ADB
from appium import webdriver

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')

filelist = os.listdir(r'C:\Users\youwei\Desktop\packagefile')

resultlist = []

def test():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    #desired_caps['deviceName'] = '4df727dd1300bf99' #三星s3
    #desired_caps['deviceName'] ='P4M0215216007050' #华为mate7
    desired_caps['deviceName'] ='05157df510243104' #三星s6
    desired_caps['appPackage'] = 'com.moji.mjweather'
    desired_caps['appActivity'] = 'com.moji.mjweather.activity.main.MainActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboaed'] = 'True'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    time.sleep(5)

    driver.tap([(762,1260)],50)
    time.sleep(2)

    #driver.tap([(762,1260)],50)

    #driver.swipe(960,1000,100,1000)
    #driver.swipe(960,1000,100,1000)
    #driver.tap([(720,1900)],50)
    #time.sleep(1)

    driver.find_element_by_name(u"我").click()
    time.sleep(1)
    driver.swipe(500,1600,500,400)
    driver.find_element_by_id('com.moji.mjweather:id/bl_owner_home_pager_setting').click()
    time.sleep(1)
    driver.swipe(500,1700,500,200)
    time.sleep(1)
    driver.find_element_by_id('com.moji.mjweather:id/rl_about').click()
    time.sleep(1)
    element = driver.find_element_by_id('com.moji.mjweather:id/about_text_version')
    resultlist.append(element.text)
    time.sleep(1)
    driver.quit()

def main():
    for eachpackage in filelist:
        os.system(r'adb install C:\Users\youwei\Desktop\packagefile\%s' % eachpackage)
        #install_infor = os.popen('adb install %s' % eachpackage)
        #print 'install status : %s' % install_infor.read()

        test()

        os.system('adb uninstall com.moji.mjweather')
        #uninstall_infor = os.popen('adb uninstall com.moji.mjweather')
        #print 'uninstall status : %s' % uninstall_infor.read()
        myadb.shell_command('rm -r sdcard/moji')
        time.sleep(2)

    mydict = dict(zip(filelist,resultlist))


if __name__ == '__main__':
    main()
