from pyadb.adb import ADB

myadb = ADB('E:\\adt-bundle-windows\\sdk\\platform-tools\\adb')

myadb.shell_command('rm -r sdcard/moji')
