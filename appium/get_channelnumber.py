_author = 'wangyouwei'
#-*- coding:utf8 -*-

import os
import time
from pyadb.adb import ADB
from appium import webdriver
from selenium.webdriver.common.by import By

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')

filelist = os.listdir(r'C:\Users\youwei\Desktop\speicalpackage')

resultlist = []

#继承父类，改写方法. Remote类实为selenium.webdriver.wedriver  被appium.webdriver 初始化 import 为 Remote
class mywebdriver(webdriver.Remote):
    def __init__(self, mycommand_executor='http://127.0.0.1:4444/wd/hub',
        mydesired_capabilities=None, mybrowser_profile=None, myproxy=None, mykeep_alive=False):
        super(mywebdriver,self).__init__(mycommand_executor,
        mydesired_capabilities, mybrowser_profile, myproxy, mykeep_alive)

    def find_element_by_id(self, id_,waittime=1):

        time.sleep(waittime)
        print 'wait 1s'
        return self.find_element(by=By.ID, value=id_)



def test():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    #desired_caps['deviceName'] = '4df727dd1300bf99' #三星s3
    #desired_caps['deviceName'] ='P4M0215216007050' #华为mate7
    desired_caps['deviceName'] ='05157df510243104' #三星s6
    desired_caps['appPackage'] = 'com.moji.mjweather'
    desired_caps['appActivity'] = 'com.moji.mjweather.activity.main.MainActivity'
    #desired_caps['appActivity'] = 'com.moji.mjweather.activity.main.AddCityFragmentActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboaed'] = 'True'

    #driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = mywebdriver('http://localhost:4723/wd/hub', desired_caps)

    time.sleep(5)

    driver.tap([(762,1260)],50)
    time.sleep(3)

    #driver.tap([(762,1260)],50)

    #driver.swipe(960,1000,100,1000)
    #driver.swipe(960,1000,100,1000)
    #driver.tap([(720,1900)],50)
    #time.sleep(1)

    #driver.implicitly_wait(5)
    driver.find_element_by_name(u"我").click()
    time.sleep(1)
    driver.swipe(500,1600,500,400)
    time.sleep(1)
    driver.find_element_by_id('com.moji.mjweather:id/bl_owner_home_pager_setting').click()

    driver.swipe(500,1700,500,200)
    time.sleep(2)
    driver.find_element_by_id('com.moji.mjweather:id/rl_about').click()

    element = driver.find_element_by_id('com.moji.mjweather:id/about_text_version')
    resultlist.append(element.text)


    #driver.reset()
    driver.close_app()
    driver.quit()
    time.sleep(1)

def main():
    for eachpackage in filelist:
        #os.system(r'adb install C:\Users\youwei\Desktop\firstpackage\%s' % eachpackage)
        install_infor = os.popen(r'adb install C:\Users\youwei\Desktop\speicalpackage\%s' % eachpackage)
        print 'install status : %s' % install_infor.read()
        time.sleep(1)
        test()
        #os.system('adb uninstall com.moji.mjweather')
        uninstall_infor = os.popen('adb uninstall com.moji.mjweather')
        print 'uninstall status : %s' % uninstall_infor.read()
        myadb.shell_command('rm -r sdcard/moji')
        time.sleep(1)

    mydict = dict(zip(filelist,resultlist))
    for key in mydict:
        print key,mydict[key]

if __name__ == '__main__':
    main()
