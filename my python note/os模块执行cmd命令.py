# -* coding:utf-8 *-

#调用os执行win系统命令
import os
import commands

os.system('ping www.baidu.com')#无返回值

out = os.popen('ping www.baidu.com')
print out.read() #控制台输出

'''
#commands 只能linux下使用
(status, output) = commands.getstatusoutput('ipconfig')
print status, output
'''
