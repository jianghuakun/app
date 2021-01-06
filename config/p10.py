#!/usr/bin/python3
import uiautomator2 as u2
import unittest
import time
import os
class p10():
    # 初始化手机端uiautomator2
    os.system('python -m uiautomator2 init')
    time.sleep(2)
    # 启动手机端ATX
    os.system('adb shell am start -n  com.github.uiautomator/.MainActivity')

    # 点击手机端uiautomator
    os.system('adb shell input tap 500 500')
    d = u2.connect('192.168.2.133')
    d.healthcheck() # 解锁屏幕并启动uiautomator服务
