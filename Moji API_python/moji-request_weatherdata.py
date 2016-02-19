# -*- coding:utf8 -*-

import urllib2
import httplib
import json

url = 'http://weather.moji.com/weather/pb/detail'

values = {"common":{"identifier":"866926020778063","app_version":"10058703","os_version":"21","device":"NX510J","platform":"Android","pid":"5000","language":"CN","uid":"257390811","width":1080,"height":1920},"params":{"city":[{"id":340,"ts":1454645364825,"avatarId":29,"cr":1}],"fst":0,"sst":1454645365496,"tu":"c","wu":"beau","lang":"CN"},"added":{"rtCount":0,"uptype":1,"net":"WIFI","pkg":"com.moji.mjweather"}}

headers = {'Content-Type':'application/json','Content-Length':361,'Host':'weather.moji.com','Connection':'Keep-Alive','User-Agent':'Apache-HttpClient/UNAVAILABLE(java 1.4)'}

data = json.dumps(values)

try:
    request = urllib2.Request(url,headers)
    response = urllib2.urlopen(request,data)
except Exception, e:
    pass
    #print e
else:
    print repr(response.read())
    print 'Data request finish!'
    
#connect = httplib.HTTPConnection('weather.moji.com')
#connect.request(method='post',url=url,body=data,headers=headers)
#response = connect.getresponse()
#connect.close()

#print response.read()

#IDLE输出
#print repr(response.read())
