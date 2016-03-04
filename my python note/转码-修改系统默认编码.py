#-*- coding:utf8 -*-

import sys

#查看python默认编码
sys.getdefaultencoding()

#保存系统输出
stdin,stdout,stderr = sys.stdin,sys.stdout,sys.stderr

#重新加载模块，修改默认编码
reload(sys)
sys.setdefaultencoding('utf8')
#重定向输出
sys.stdin,sys.stdout,sys.stderr = stdin,stdout,stderr

#u'我' 应等于 '我'.decode('gbk')
#str类型包括：utf-8 gbk等
#decode解码为unicode，然encode转码
