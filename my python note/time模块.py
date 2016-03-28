import datetime
import time

print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print datetime.datetime.now()
print time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
