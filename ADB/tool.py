# -*- coding:gbk -*-
_author = 'wangyouwei'
import os, sys
from pyadb.adb import ADB

def has(arg):
    if 'package:'+arg in applist:
        if arg == 'com.moji.mjweather':
            print '    moji_weather already exist'
            return True
        if arg == 'com.moji.wallpaper':
            print '    moji_paper already exist'
            return True
    else:
        if arg == 'com.moji.mjweather':
            print '    moji_weather NOT exist'
            return False
        if arg == 'com.moji.wallpaper':
            print '    moji_paper NOT exist'
            return False

def check_weather():
    return has('com.moji.mjweather')

def check_paper():
    return has('com.moji.wallpaper')

def install_app():
    path = os.getcwd()
    filelist = os.listdir(path)
    for num,filename in enumerate(filelist):
        print '    ',num,' . ',filename
    choice = raw_input('    please enter number:')
    if int(choice) >= len(filelist):
        print '    input number out of index!'
    else:
        stdout = os.popen(r'adb install %s/%s' % (path,filelist[int(choice)]))
        print '    ',stdout.read()


def del_weather():
    stdout = os.popen('adb uninstall com.moji.mjweather')
    os.popen(r'adb shell rm -r sdcard/moji')
    print '    ',stdout.read()

def del_paper():
    stdout = os.popen('adb uninstall com.moji.wallpaper')
    os.popen(r'adb shell rm -r sdcard/wallpaper')
    print '    ',stdout.read()

def get_cpu(arg):
    #stdout = os.popen(r'adb shell cat /proc/cpuinfo')
    #print '    ',stdout.read()
    myadb.shell_command('top -n 5|grep %s' % arg)
    print myadb.get_output()

def get_memory(arg):
    stdout = os.popen('adb shell dumpsys meminfo %s' % arg)
    print '    ',stdout.read()

def run(arg):
    if arg==1:
        check_weather()
    if arg==2:
        check_paper()
    if arg==3:
        install_app()
    if arg==4:
        if check_weather():
            del_weather()
    if arg==5:
        if check_paper():
            del_paper()
    if arg==6:
        print '   ',66666666666
    if arg==7:
        if check_weather():
            get_cpu('com.moji.mjweather')
    if arg==8:
        if check_weather():
            get_memory('com.moji.mjweather')
    if arg==9:
        if check_paper():
            get_cpu('com.moji.wallpaper')
    if arg==10:
        if check_paper():
            get_memory('com.moji.wallpaper')
    if arg==11:
        sys.exit()

def main():
    print '''
    ***************MY TOOLS***************
    1.检查墨迹天气是否安装
    2.检查墨迹壁纸是否安装
    3.安装墨迹天气或墨迹壁纸
    4.卸载墨迹天气
    5.卸载墨迹壁纸
    6.
    7.查询墨迹天气占用cpu信息
    8.查询墨迹天气占用内存信息
    9.查询墨迹壁纸占用cpu信息
    10.查询墨迹壁纸占用内存信息
    11.退出
    ***************MY TOOLS***************
    '''
    select = raw_input('    请输入数字选择功能：')
    try:
        number = int(select)
        if number>11:
            raise IndexError
    except Exception:
        print '    输入错误,请重新输入!'
        print
    else:
        run(number)


if __name__ == '__main__':
    myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')

    while True:
        applist = os.popen(r'adb shell pm list package').read()
        main()
