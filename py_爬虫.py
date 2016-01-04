# -*- coding:UTF-8 -*-
'''
import requests
#链接：http://www.zhihu.com/question/36044851/answer/65629497
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
r = requests.get('http://www.zhihu.com/question/36044851/answer/65625801')  # 发送请求
print r.status_code  # 返回码 
print r.headers['content-type']  # 返回头部信息
print r.encoding  # 编码信息
print r.text #内容部分
'''
'''
#爬取页面titile
from bs4 import BeautifulSoup
import urllib2
import sys
import HTMLParser
reload(sys)
sys.setdefaultencoding("utf-8")
url = 'http://tieba.baidu.com/f?ie=utf-8&kw=snh48&fr=search'
htmlpage = urllib2.urlopen(url).read()
soup = BeautifulSoup(htmlpage)
titles = soup.findAll('a', attrs={'class' : 'j_th_tit' })
for title in titles:
        subUrl ='http://tieba.baidu.com/'+title.get('href')
        subhtmlpage = urllib2.urlopen(subUrl).read()
        subsoup = BeautifulSoup(subhtmlpage)
        titles2 = subsoup.findAll('h1', attrs={'class' : 'core_title_txt'})
        for subtile in titles2:
           print subtile.get('title')
'''

import requests
import threading
from bs4 import BeautifulSoup
import re

"""
Description    : 将网页图片保存本地
@param imgUrl  : 待保存图片URL
@param imgName : 待保存图片名称
@return 无
"""
def saveImage( imgUrl,imgName ="default.jpg" ):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir="C:\\Users\\youwei\\Desktop\\imgs\\"
    print 'save'+DstDir+imgName+'\n'
    try:
        with open(DstDir+imgName ,"wb") as jpg:
            jpg.write(image)     
            return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close        

"""
Description    : 开启多线程执行下载任务
@param filelist:待下载图片URL列表
@return 无
"""

def downImageViaMutiThread( filelist ):
    task_threads=[]  #存储线程
    count=1
    for file in filelist:
        filename = file.replace("/","-")
        if 'com-' in filename:
            p = re.compile(r'com-')
            print(filename)        
            filename = p.split(filename)[1]
            t = threading.Thread(target=saveImage,args=(file,filename))
            count = count+1
            task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join() 

"""
Description    : 获取图片地址
@param pageUrl : 网页URL
@return : 图片地址列表
"""

def getfilelist(pageUrl):
    web = requests.get(pageUrl)
    soup = BeautifulSoup(web.text)
    filelist=[]
#   for photo in soup.find_all('img',{'class':'scrollLoading'}):
    for photo in soup.find_all('img'):
        filelist.append(photo.get('src'))
#        filelist.append(photo.get('data-original'))
    return filelist

def getweblist(webUrl):
    web = requests.get(webUrl)
    soup = BeautifulSoup(web.text)
    weblist=[]
    for pagelist in soup.find_all('div',{'class':'metaRight'}):
        for link in pagelist.find_all('a'):
            weblist.append(link.get('href'))
    return weblist  

if __name__ == "__main__":
  webUrl = 'http://www.meizitu.com/'
  list = getweblist(webUrl)
  for page in list:
    imagelist=getfilelist(page)
    downImageViaMutiThread(imagelist)