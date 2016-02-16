_author = 'wangyouwei'
from pyadb.adb import ADB
import os

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')
#stdout = os.popen('adb uninstall com.moji.mjweather')
stdout = os.popen('adb devices')
print stdout.read()
myadb.shell_command('rm -r sdcard/moji')
myadb.shell_command('rm -r sdcard/wallpaper')

