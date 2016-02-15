from pyadb.adb import ADB
import os

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')
myadb.shell_command('rm -r sdcard/moji')
myadb.shell_command('rm -r sdcard/wallpaper')
