# -*- coding:utf8 -*-

import urllib2
import json

#PSOT
url = 'http://lbs.moji.com/location/json/query'
values = {
    'common': {
        'uid': '238411863',
        'platform': 'Android',
        'height': 1920,
        'width': 1080,
        'device': 'HUAWEI MT7-TL00',
        'app_version': '10058703',
        'pid': '5000',
        'language': 'CN',
        'identifier': '865166026924624',
        'os_version': '19'
    },
    'params': {
        'coordinate_system': 2,
        'longitude': 116.490529,
        'latitude': 39.972809,
        'location': '北京市朝阳区酒仙桥路',
        'ip': '192.168.10.94'
    }
}

headers = {'Content-Type':'application/json','Content-Length':374,'Host':'lbs.moji.com','Connection':'Keep-Alive','User-Agent':'Apache-HttpClient/UNAVAILABLE(java 1.4)'}

data = json.dumps(values)

try:
    request = urllib2.Request(url,headers)
    response = urllib2.urlopen(request,data)
except Exception, e:
    pass
    #print e
else:
    print response.read()
    print 'Data request finish!'
