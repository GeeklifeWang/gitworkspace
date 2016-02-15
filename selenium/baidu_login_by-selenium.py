#-*- coding:utf-8 -*-
import time
import os
from selenium import webdriver

os.environ['webdriver.chrome.driver'] = 'D:\\Chrome31\\chromedriver'
chromepath = 'D:\\Chrome31\\chromedriver'
browser = webdriver.Chrome(chromepath)

#iepath = 'C:\\Program Files (x86)\\Internet Explorer 11\\iexplore.exe'
#browser = webdriver.Ie(iepath)

browser.get('http://www.baidu.com')

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.maximize_window()

time.sleep(1)

browser.find_element_by_name('tj_login').click()

time.sleep(1)

#browser.find_elements_by_name('userName').clear()

browser.find_element_by_name('userName').send_keys('18610046959')
browser.find_element_by_name('password').send_keys('199308060036')
browser.find_element_by_id('TANGRAM__PSP_8__submit').click()

time.sleep(10)

browser.close()
browser.quit()

print 'finish.'


#传值点击
#driver.find_element_by_id('').send_keys('')
#driver.find_element_by_id('').click()

#右键点击
#driver.ActionChains.context_click()
#双击
#driver.ActionChains.double_click()

