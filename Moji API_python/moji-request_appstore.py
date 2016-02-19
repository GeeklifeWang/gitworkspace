# -*- coding:utf8 -*-

import urllib
import urllib2

#GET
url = 'http://register.moji001.com/weather/RegisterUser?ID=0&UserID=&Platform=Android&Device=phone&Version=10058703&VerNo=10058703&APILevel=21&SdkVer=5.0.2&IMEI=866926020778063&Model=NX510J&MAC=d8:55:a3:de:b3:9d&PartnerID=5000&DBVerNo=1'

#url = 'http://app.moji001.com/appstore/message'

#values = {'AppId':'','Platform':1000,'Device':'phone','OsVersion':19,'Model':'HUAWEI+MT7-TL00','Location':600,'UserId':238411863,'Mversion':10058502,'PartnerID':5007,'IMEI':865166026924624}

#headers = {'Accept-Encoding':'gzip,deflate','Host':'app.moji001.com','Connection':'Keep-Alive','User-Agent':'Apache-HttpClient/UNAVAILABLE(java 1.4)'}

#data = urllib.urlencode(values)

#request = urllib2.Request(url,data,headers)
#response = urllib2.urlopen(requset)

try:
    response = urllib2.urlopen(url)
except Exception, e:
    pass
    #print e
else:
    print response.read()
    print 'Data request finish!'
