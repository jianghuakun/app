#!/usr/bin/python3
import uiautomator2 as u2
import unittest
import time
import os
from config.p10 import p10
#本实例为adb+uiautomator2自动化测试app基本操作。必须要先初始化手机端uiautomator2
'''
d = u2.connect('10.0.0.170')
# 启动App
d.app_start("com.huiti.score")
import uiautomator2 as u2
'''
'''
#初始化手机端uiautomator2
os.system('python -m uiautomator2 init')
time.sleep(2)
#启动手机端ATX
os.system('adb shell am start -n  com.github.uiautomator/.MainActivity')

#点击手机端uiautomator
os.system('adb shell input tap 500 500')
d = u2.connect('10.0.0.170')
'''
d=p10.d
print(d.info)
time.sleep(2)
#启动app
r=d.app_start("com.huiti.score")
print(r)
time.sleep(2)
#r1=d(resourceId="com.huiti.score:id/main_create_race").click
#点击添加活动
addfootball=os.system('adb shell input tap 500 1800')
time.sleep(2)
#创建足球比赛
os.system('adb shell input tap 200 800')
time.sleep(2)
#选择主队
os.system('adb shell input tap 1000 300')
time.sleep(2)
#点击选择已存在球队
os.system('adb shell input tap 600 300')
time.sleep(2)
#点击球队选择
os.system('adb shell input tap 500 900')
time.sleep(2)
#选择客队
os.system('adb shell input tap 1000 500')
time.sleep(2)
#点击选择已存在球队
os.system('adb shell input tap 600 300')
time.sleep(2)
#点击球队选择
os.system('adb shell input tap 500 600')
time.sleep(2)
#选择开始时间
os.system('adb shell input tap 500 700')
time.sleep(2)
#确定时间
os.system('adb shell input tap 1000 1400')
time.sleep(2)
#选择结束时间
#os.system('adb shell input tap 1000 300')
time.sleep(2)
#点击选择学校场地
os.system('adb shell input tap 900 1000')
time.sleep(2)
#选择场地
os.system('adb shell input tap 1000 1500')
time.sleep(2)
#点击确定
os.system('adb shell input tap 1000 1100')
time.sleep(2)

#确定
os.system('adb shell input tap 500 1800')
time.sleep(1)
#print(r1)
#停止uiautomator
os.system('adb shell input tap 700 500')
#关闭ATX
os.system('adb shell am force-stop com.github.uiautomator')
#关闭app
#d.app_stop("com.huiti.score")
