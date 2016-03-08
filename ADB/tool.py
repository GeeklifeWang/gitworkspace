# -*- coding:gbk -*-
_author = 'wangyouwei'
import os, sys,re
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

def get_liuliang(arg):
    myadb.shell_command('top -n 2|grep %s' % arg)
    deal_list=myadb.get_output().split(' ')
    for i in deal_list:
        if i.startswith('u0_'):
            result_str = i
            #print '    ',result_str
            break
    m = re.match(r'u0_a(\d+)',result_str)
    uid = m.group(1)
    choice = raw_input('    �Ƿ����ԭʼ��������? y/n:')
    if choice.lower() == 'y':
        os.popen(r'adb shell rm -rf /proc/uid_stat/10%s/*' % uid)
    #print '    ',uid
    myadb.shell_command(r'cat /proc/uid_stat/10%s/tcp_rcv' % uid)
    receive = myadb.get_output()
    myadb.shell_command(r'cat /proc/uid_stat/10%s/tcp_snd' % uid)
    send = myadb.get_output()
    final = (int(receive) - int(send))/1024
    print '    ',final,'MB'

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
        if check_weather():
            get_liuliang('com.moji.mjweather')
    if arg==7:
        if check_paper():
            get_liuliang('com.moji.wallpaper')
    if arg==8:
        if check_weather():
            get_cpu('com.moji.mjweather')
    if arg==9:
        if check_weather():
            get_memory('com.moji.mjweather')
    if arg==10:
        if check_paper():
            get_cpu('com.moji.wallpaper')
    if arg==11:
        if check_paper():
            get_memory('com.moji.wallpaper')
    if arg==12:
        sys.exit()

def main():
    print '''
    ***************MY TOOLS***************
    1.���ī�������Ƿ�װ
    2.���ī����ֽ�Ƿ�װ
    3.��װī��������ī����ֽ
    4.ж��ī������
    5.ж��ī����ֽ
    6.��ѯī��������������
    7.��ѯī����ֽ��������
    8.��ѯī������ռ��cpu��Ϣ
    9.��ѯī������ռ���ڴ���Ϣ
    10.��ѯī����ֽռ��cpu��Ϣ
    11.��ѯī����ֽռ���ڴ���Ϣ
    12.�˳�
    ***************MY TOOLS***************
    '''
    select = raw_input('    ����������ѡ���ܣ�')
    try:
        number = int(select)
        if number>11:
            raise IndexError
    except Exception:
        print '    �������,����������!'
        print
    else:
        run(number)


if __name__ == '__main__':
    myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')
    while True:
        applist = os.popen(r'adb shell pm list package').read()
        main()
