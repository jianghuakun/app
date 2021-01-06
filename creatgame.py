
#!/usr/bin/python3
import os
import time
import datetime
#打开app
starttime = datetime.datetime.now()

#long running

tic = time.clock()
os.system('adb shell am start -n com.huiti.score/.HTWelcomeActivity')
toc = time.clock()
print('单次处理时长: ' + '%.2f' % (toc - tic) + ' s')

time.sleep(2)
#os.system('adb shell input tap 600 300')
#点击增加比赛按钮
addfootball=os.system('adb shell input tap 500 1800')
#addfootball=os.popen('adb shell input tap 500 1900').read()
time.sleep(2)
print(addfootball)
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

#关闭app
os.system('adb shell am force-stop com.huiti.score')