# -*- coding:UTF-8 -*-
'''
from xlwt import Workbook, Formula
import xlrd
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0,0,"                   adasfaxcc   asfca    ascd")
sheet1.write(1,0,"                   asdasd      asdas  asascd")


sheet2 = book.add_sheet('Sheet 2')
row = sheet2.row(0)
row.write(0,Formula('1'))
row.write(1,Formula('2'))
row.write(2,Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$b$2)"))

book.save('1.xls')

book = xlrd.open_workbook('1.xls')
sheet = book.sheets()[0]
nrows=sheet.nrows
ncols=sheet.ncols
for i in range(nrows):
    for j in range(ncols):
        print (sheet.cell(i,j).value)
'''

import turtle
import random
turtle.pensize(2)
turtle.color("green")

x=-240
y=-240
turtle.up()

turtle.goto(x,y)
for m in range(0,17):
    turtle.speed(1000)
    turtle.down()
    turtle.forward(480)
    turtle.up()
    y=y+30
    turtle.goto(x,y)
turtle.up

y=y-30
turtle.goto(x,y)
turtle.right(90)
for n in range(0,17):
    turtle.down()
    turtle.forward(480)
    turtle.up()
    x=x+30
    turtle.goto(x,y)
turtle.up()#回到起点
turtle.goto(0,0)
turtle.pensize(5)
turtle.color("black")
turtle.pendown()




turtle.speed(5)
a=30
b=-30
x=0
y=0
    #c=0
    #(x,y)=(x+a,y) or (x+b,y) or (x,y+a) or (x,y+b)
listway = [(1,1)]
(x,y)=(0,0)
for d in range(0,1001):
    if (x,y) not in listway[0]:
        (x,y)=random.choice([(x+a,y) ,(x+b,y) ,(x,y+a) , (x,y+b)])
        turtle.goto(x,y)
        listway.append((x,y))
        #continue
    if(x==240 or x==-240 or y==240 or y==-240):
        
        break
        print("Game Over")
