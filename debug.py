#!/usr/bin/python3
import json
import unittest
#from config.headers import headers
#from config.runmethon import runmethon
import unittest
from config.HTMLTestRunner import HTMLTestRunner
import time
# 相对路径
test_dir =r'./'
test_dir1 =r'./report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_2_web*.py')
if __name__ == '__main__':
    # 定义带有当前测试时间的报告，防止前一次报告被覆盖
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + ' testReport.html'
    # 二进制打开，准备写入文件
    fp = open('./report/{0}'.format(filename), 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试执行情况')
    runner.run(discover)
    fp.close()
