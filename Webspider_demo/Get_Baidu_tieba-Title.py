_author = 'wangyouwei'
#-*- coding:utf-8 -*-
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
