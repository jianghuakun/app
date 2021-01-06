#!/usr/bin/python3
import uiautomator2 as u2
import time
import unittest
d = u2.connect()
d(text='Via').click()
d(text='Via').click(timeout=10) #等10秒如果目标还不出现，报错吧
d(text="Skip").click_gone(maxretry=10, interval=1.0)
# maxretry default 10, interval default 1.0目前在的话，每隔1秒点一次，共点10次。
d(text='Skip').click_exists(timeout=10.0)
 #存在10秒之后点击，默认是0秒（一出现就点）
d.double_click(x, y, 0.1) #双击，默认每次间隔 0.1s
d.long_click(x, y, 0.5) #长摁，默认0.5s
d.swipe(sx, sy, ex, ey, 0.5) # 滑动，for 0.5s(default)
d.drag(sx, sy, ex, ey, 0.5) #拖拽 for 0.5s(default)
d.swipe((x0, y0), (x1, y1), (x2, y2), 0.2) #解锁屏，九宫格用