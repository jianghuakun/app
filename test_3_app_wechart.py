#!/usr/bin/python3
import uiautomator2 as u2
import time
import unittest
class wechart1(unittest.TestCase):
    """微信分享"""
    def setUp(self):
        print("app微信分享开始")

    def test_wechart_1(self):
        """已结束列表界面分享"""
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
        # d.xpath('//*[@text="智慧校园运动场"]').click()
        #切换到已结束
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_end_tab"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="切换已结束Fail"):
                self.assertEqual(0, 1, "切换已结束Fail")
        else:
            with self.subTest(data="切换已结束PASS"):
                self.assertEqual(0, 0, "切换已结束PASS")
        #点击收藏、复制、分享按钮
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_end_match_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击收藏、复制、分享按钮Fail"):
                self.assertEqual(0, 1, "点击收藏、复制、分享按钮Fail")
        else:
            with self.subTest(data="点击收藏、复制、分享按钮PASS"):
                self.assertEqual(0, 0, "点击收藏、复制、分享按钮PASS")
        #点击分享按钮
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/tv_share"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击分享按钮Fail"):
                self.assertEqual(0, 1, "点击分享按钮Fail")
        else:
            with self.subTest(data="点击分享按钮PASS"):
                self.assertEqual(0, 0, "点击分享按钮PASS")
        #点击分享微信好友
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_share_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="点击分享微信好友Fail"):
                self.assertEqual(0, 1, "点击分享微信好友Fail")
        else:
            with self.subTest(data="点击分享微信好友PASS"):
                self.assertEqual(0, 0, "点击分享微信好友PASS")
        #点击搜索按钮
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/g_5"]/android.widget.LinearLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击搜索按钮Fail"):
                self.assertEqual(0, 1, "点击搜索按钮Fail")
        else:
            with self.subTest(data="点击搜索按钮PASS"):
                self.assertEqual(0, 0, "点击搜索按钮PASS")
        #点击搜索输入框
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/bfl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击搜索输入框Fail"):
                self.assertEqual(0, 1, "点击搜索输入框Fail")
        else:
            with self.subTest(data="点击搜索输入框pass"):
                self.assertEqual(0, 0, "点击搜索输入框pass")
        #输入需要发送的微信号
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/bfl"]').set_text("江")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入需要发送的微信号Fail"):
                self.assertEqual(0, 1, "输入需要发送的微信号Fail")
        else:
            with self.subTest(data="输入需要发送的微信号PASS"):
                self.assertEqual(0, 0, "输入需要发送的微信号PASS")
        #点击选择需要发送的微信
        try:
            d.xpath(
                '//*[@resource-id="com.tencent.mm:id/f76"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击选择需要发送的微信Fail"):
                self.assertEqual(0, 1, "点击选择需要发送的微信Fail")
        else:
            with self.subTest(data="点击选择需要发送的微信PASS"):
                self.assertEqual(0, 0, "点击选择需要发送的微信PASS")
        #点击分享按钮完成微信分享
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/dm3"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击分享按钮完成微信分享Fail"):
                self.assertEqual(0, 1, "点击分享按钮完成微信分享Fail")
        else:
            with self.subTest(data="点击分享按钮完成微信分享PASS"):
                self.assertEqual(0, 0, "点击分享按钮完成微信分享PASS")
        #微信分享结果判断
        try:
            wetext=d.xpath('//*[@resource-id="com.tencent.mm:id/awj"]').get_text()
            time.sleep(2)
            if wetext=="已发送":
                with self.subTest(data="微信分享PASS"):
                    self.assertEqual(0, 0, "微信分享PASS")
            else:
                with self.subTest(data="微信分享Fail"):
                    self.assertEqual(0, 0, "微信分享Fail")

        except Exception as e:
            with self.subTest(data="微信分享异常"):
                self.assertEqual(0, 1, "微信分享异常")
        else:
            pass
        #返回app
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/dlq"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="返回app Fail"):
                self.assertEqual(0, 1, "返回app Fail")
        else:
            with self.subTest(data="返回app pass"):
                self.assertEqual(0, 0, "返回app pass")
        #关闭app
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")
    def test_wechart_2(self):
        """未结束列表分享"""
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
        # d.xpath('//*[@text="智慧校园运动场"]').click()
        #切换到已结束
        '''
                try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_end_tab"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="切换已结束Fail"):
                self.assertEqual(0, 1, "切换已结束Fail")
        else:
            with self.subTest(data="切换已结束PASS"):
                self.assertEqual(0, 0, "切换已结束PASS")
        '''

        #点击收藏、复制、分享按钮
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_unend_match_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击收藏、复制、分享按钮Fail"):
                self.assertEqual(0, 1, "点击收藏、复制、分享按钮Fail")
        else:
            with self.subTest(data="点击收藏、复制、分享按钮PASS"):
                self.assertEqual(0, 0, "点击收藏、复制、分享按钮PASS")
        #点击分享按钮
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/tv_share"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击分享按钮Fail"):
                self.assertEqual(0, 1, "点击分享按钮Fail")
        else:
            with self.subTest(data="点击分享按钮PASS"):
                self.assertEqual(0, 0, "点击分享按钮PASS")
        #点击分享微信好友
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_share_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="点击分享微信好友Fail"):
                self.assertEqual(0, 1, "点击分享微信好友Fail")
        else:
            with self.subTest(data="点击分享微信好友PASS"):
                self.assertEqual(0, 0, "点击分享微信好友PASS")
        #点击搜索按钮
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/g_5"]/android.widget.LinearLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击搜索按钮Fail"):
                self.assertEqual(0, 1, "点击搜索按钮Fail")
        else:
            with self.subTest(data="点击搜索按钮PASS"):
                self.assertEqual(0, 0, "点击搜索按钮PASS")
        #点击搜索输入框
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/bfl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击搜索输入框Fail"):
                self.assertEqual(0, 1, "点击搜索输入框Fail")
        else:
            with self.subTest(data="点击搜索输入框pass"):
                self.assertEqual(0, 0, "点击搜索输入框pass")
        #输入需要发送的微信号
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/bfl"]').set_text("江")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入需要发送的微信号Fail"):
                self.assertEqual(0, 1, "输入需要发送的微信号Fail")
        else:
            with self.subTest(data="输入需要发送的微信号PASS"):
                self.assertEqual(0, 0, "输入需要发送的微信号PASS")
        #点击选择需要发送的微信
        try:
            d.xpath(
                '//*[@resource-id="com.tencent.mm:id/f76"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击选择需要发送的微信Fail"):
                self.assertEqual(0, 1, "点击选择需要发送的微信Fail")
        else:
            with self.subTest(data="点击选择需要发送的微信PASS"):
                self.assertEqual(0, 0, "点击选择需要发送的微信PASS")
        #点击分享按钮完成微信分享
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/dm3"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击分享按钮完成微信分享Fail"):
                self.assertEqual(0, 1, "点击分享按钮完成微信分享Fail")
        else:
            with self.subTest(data="点击分享按钮完成微信分享PASS"):
                self.assertEqual(0, 0, "点击分享按钮完成微信分享PASS")
        #微信分享结果判断
        try:
            wetext=d.xpath('//*[@resource-id="com.tencent.mm:id/awj"]').get_text()
            time.sleep(2)
            if wetext=="已发送":
                with self.subTest(data="微信分享PASS"):
                    self.assertEqual(0, 0, "微信分享PASS")
            else:
                with self.subTest(data="微信分享Fail"):
                    self.assertEqual(0, 0, "微信分享Fail")

        except Exception as e:
            with self.subTest(data="微信分享异常"):
                self.assertEqual(0, 1, "微信分享异常")
        else:
            pass
        #返回app
        try:
            d.xpath('//*[@resource-id="com.tencent.mm:id/dlq"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="返回app Fail"):
                self.assertEqual(0, 1, "返回app Fail")
        else:
            with self.subTest(data="返回app pass"):
                self.assertEqual(0, 0, "返回app pass")
        #关闭app
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")

    def tearDown(self):
        '''微信分享测试结束'''

