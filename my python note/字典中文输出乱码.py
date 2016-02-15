# -*- coding:utf8 -*-
import json
l1 = ['一','二','三']
l2 = [1,2,3]
d = dict(zip(l1,l2))
print json.dumps(d, encoding='utf-8', ensure_ascii=False) 
