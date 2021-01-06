#!/usr/bin/python3
import uiautomator2 as u2
import unittest
import time
import os
#本实例为adb+uiautomator2自动化测试app基本操作。必须要先初始化手机端uiautomator2
'''
d = u2.connect('10.0.0.170')
# 启动App
d.app_start("com.huiti.score")
import uiautomator2 as u2
'''
class p10():
    # 初始化手机端uiautomator2
    os.system('python -m uiautomator2 init')
    time.sleep(2)
    # 启动手机端ATX
    os.system('adb shell am start -n  com.github.uiautomator/.MainActivity')

    # 点击手机端uiautomator
    os.system('adb shell input tap 500 500')
    d = u2.connect('10.0.0.170')
