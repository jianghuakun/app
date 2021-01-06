#!/usr/bin/python3
import uiautomator2 as u2
import time
import unittest
class loginapp(unittest.TestCase):
    """app登录测试"""
    def setUp(self):
        print("app登录测试开始")

    def test_1_app_login_1(self):
        """用户名和密码正确登录测试-登录状态退出再登录"""
        d = u2.connect()
        d.healthcheck()  # 解锁屏幕并启动uiautomator服务
        try:
            d.app_start("com.huiti.score")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="APP启动Fail"):
                self.assertEqual(0, 1, "APP启动Fail")
        else:
            with self.subTest(data="APP启动PASS"):
                self.assertEqual(0, 0, "APP启动PASS")
        #切换到我的界面
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/main_tab_account_ll"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="切换到我的界面Fail"):
                self.assertEqual(0, 1, "切换到我的界面Fail")
        else:
            with self.subTest(data="切换到我的界面PASS"):
                self.assertEqual(0, 0, "切换到我的界面PASS")

        #判断是否登录，如果登录退出
        try:
            name=d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_name_tv"]').get_text()
            time.sleep(2)
            if name=="研发稳定性测试":
                d.xpath('//*[@resource-id="com.huiti.score:id/ht_setting_rl"]').click()
                time.sleep(2)
                d.xpath('//*[@resource-id="com.huiti.score:id/ht_setting_logout"]').click()
                time.sleep(2)
                d.xpath('//*[@resource-id="com.huiti.score:id/positiveButton"]').click()
                time.sleep(2)
            else:
                pass
        except Exception as e:
            pass
        else:
            pass
        #点击登录按钮，切换到登录界面
        try:
            text_login=d.xpath('//*[@resource-id="com.huiti.score:id/ht_username_tv" and @text="登录/注册"]').get_text()
            if text_login=="登录/注册":
                d.xpath('//*[@resource-id="com.huiti.score:id/ht_username_tv" and @text="登录/注册"]').click()
                d.xpath('//*[@resource-id="com.huiti.score:id/login_inputAccount" and @text="请输入账号/手机号"]').exists()
                time.sleep(2)
                with self.subTest(data="点击登录按钮，切换到登录界面PASS"):
                    self.assertEqual(0, 0, "点击登录按钮，切换到登录界面PASS")
            else:
                pass
        except Exception as e:
            with self.subTest(data="登录注册按钮不存在"):
                self.assertEqual(0, 0, "登录注册按钮不存在")
        else:
            pass

        #点击账号框并且输入用户名
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/login_inputAccount"]').click()
            d.xpath('//*[@resource-id="com.huiti.score:id/login_inputAccount"]').set_text("jianghuakun")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击登录按钮，切换到登录界面Fail"):
                self.assertEqual(0, 1, "点击登录按钮，切换到登录界面Fail")
        else:
            with self.subTest(data="点击登录按钮，切换到登录界面PASS"):
                self.assertEqual(0, 0, "点击登录按钮，切换到登录界面PASS")
        #点击密码框并且输入密码
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ll_login"]/android.widget.LinearLayout[2]').click()
            d.xpath('//*[@resource-id="com.huiti.score:id/ll_login"]/android.widget.LinearLayout[2]').set_text("123456")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击密码框并且输入密码Fail"):
                self.assertEqual(0, 1, "点击密码框并且输入密码Fail")
        else:
            with self.subTest(data="点击密码框并且输入密码PASS"):
                self.assertEqual(0, 0, "点击密码框并且输入密码PASS")
        #点击登录按钮
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/login_submit"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击登录按钮Fail"):
                self.assertEqual(0, 1, "点击登录按钮Fail")
        else:
            with self.subTest(data="点击登录按钮PASS"):
                self.assertEqual(0, 0, "点击登录按钮PASS")
        #登录成功判断
        try:
            name=d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_name_tv"]').get_text()
            time.sleep(2)
            if name=="研发稳定性测试":
                with self.subTest(data="点击登录按钮PASS"):
                    self.assertEqual(0, 0, "点击登录按钮PASS")
            else:
                pass
        except Exception as e:
            with self.subTest(data="点击登录按钮Fail"):
                self.assertEqual(0, 1, "点击登录按钮Fail")
        else:
            pass
        #退出app
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")