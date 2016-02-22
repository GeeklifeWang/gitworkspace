#-*- coding:utf8 -*-
import MySQLdb

db = MySQLdb.Connect(host='localhost',user='root',passwd='root',db='lesson',charset='utf8')
cursor = db.cursor()

sql = 'INSERT INTO math(username,class)VALUES("liu", 1)'
#sql = 'SELECT * FROM math'

cursor.execute(sql)

#print cursor.fetchall()
db.commit()
db.close()
