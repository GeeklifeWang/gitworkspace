# -*- coding:UTF-8 -*-
#获取androidFPS值
import sys
import traceback
sys.path.append('C:\\Users\\youwei\\Desktop\\chromiummaster\\build\\android\\pylib')
import os,time
import android_commands
from perf import surface_stats_collector

resultList = []
deviceText = os.popen('adb devices')
textList = deviceText.readlines()
deviceName = textList[1].split()[0]
activityName = 'com.moji.mjweather'
adb = android_commands.AndroidCommands(deviceName)
collector = surface_stats_collector.SurfaceStatsCollector(adb)
collector.DisableWarningAboutEmptyData()
collector.Start()
#循环10次，主要方便自己的实现，其他实现方法请另行实现；
for i in range(10):
    time.sleep(0.3)
    results = collector.SampleResults()
    if not results:
        pass
    else:
        resultList.append(int(results[0].value))
        results[0].print_str()
    collector.Stop()
    a = resultList[3:-3]
    print u"平均值："+str(float(sum(a)/len(a)))+u" ; 最小值："+str(min(a))  

