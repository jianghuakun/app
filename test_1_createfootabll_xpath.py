#!/usr/bin/python3
import uiautomator2 as u2
import time
import unittest
class createfootball(unittest.TestCase):
    """app创建足球比赛"""
    def setUp(self):
        print("app创建足球比赛开始")

    def test_1_app_createfootball_1_selectteam(self):
        """创建足球比赛界面选择球队"""
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
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/main_create_race"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击创建活动Fail"):
                self.assertEqual(0, 1, "点击创建活动Fail")
        else:
            with self.subTest(data="点击创建活动PASS"):
                self.assertEqual(0, 0, "点击创建活动PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_create_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballFail"):
                self.assertEqual(0, 1, "点击footballFail")
        else:
            with self.subTest(data="点击footballPASS"):
                self.assertEqual(0, 0, "点击footballPASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_host_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击host_nameFail"):
                self.assertEqual(0, 1, "点击host_nameFail")
        else:
            with self.subTest(data="点击host_namePASS"):
                self.assertEqual(0, 0, "点击host_namePASS")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击playteam1Fail"):
                self.assertEqual(0, 1, "点击playteam1Fail")
        else:
            with self.subTest(data="点击playteam1PASS"):
                self.assertEqual(0, 0, "点击playteam1PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteam Fail"):
                self.assertEqual(0, 1, "点击guestteam Fail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_guest_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="guest_name select Fail"):
                self.assertEqual(0, 1, "点击guest_name Fail")
        else:
            with self.subTest(data="guest_name select pass"):
                self.assertEqual(0, 0, "点击guest_name pass")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击exitteam Fail"):
                self.assertEqual(0, 1, "点击exitteam Fail")
        else:
            with self.subTest(data="点击exitteam PASS"):
                self.assertEqual(0, 0, "点击exitteam PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteamFail"):
                self.assertEqual(0, 1, "点击guestteamFail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_start_time_rl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击starttime Fail"):
                self.assertEqual(0, 1, "点击starttime Fail")
        else:
            with self.subTest(data="点击starttime PASS"):
                self.assertEqual(0, 0, "点击starttime PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/btn_sure"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击timesure Fail"):
                self.assertEqual(0, 1, "点击timesure Fail")
        else:
            with self.subTest(data="点击timesure PASS"):
                self.assertEqual(0, 0, "点击timesure PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_place"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placeFail"):
                self.assertEqual(0, 1, "点击placeFail")
        else:
            with self.subTest(data="点击place PASS"):
                self.assertEqual(0, 0, "点击place PASS")


        try:
            d.swipe(0, 1491, 0, 1634, 0.5)  # 滑动选择153测试站点，for 0.5s(default)
            time.sleep(2)
            #d.xpath('//*[@text="153测试"]')
            s1=d.xpath('//*[@text="153测试"]').get_text()
            if s1=="153测试":
                with self.subTest(data="滑动选择153测试站点 pass"):
                    self.assertEqual(0, 0, "滑动选择153测试站点 pass")
            else:
                with self.subTest(data="滑动选择153测试站点 fail"):
                    self.assertEqual(0, 1, "滑动选择153测试站点 fail")
        except Exception as e:
            with self.subTest(data="滑动选择153测试站点 Fail"):
                self.assertEqual(0, 1, "滑动选择153测试站点 Fail")
        else:
            with self.subTest(data="滑动选择153测试站点 PASS"):
                self.assertEqual(0, 0, "滑动选择153测试站点 PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_type_confirm"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placesure Fail"):
                self.assertEqual(0, 1, "点击placesure Fail")
        else:
            with self.subTest(data="点击placesure PASS"):
                self.assertEqual(0, 0, "点击placesure PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballsure Fail"):
                self.assertEqual(0, 1, "点击footballsure Fail")
        else:
            with self.subTest(data="点击footballsure PASS"):
                self.assertEqual(0, 0, "点击footballsure PASS")
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")
    def test_1_app_createfootball_2_inputteam(self):
        """创建足球比赛界面直接输入球队"""
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
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/main_create_race"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击创建活动Fail"):
                self.assertEqual(0, 1, "点击创建活动Fail")
        else:
            with self.subTest(data="点击创建活动PASS"):
                self.assertEqual(0, 0, "点击创建活动PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_create_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballFail"):
                self.assertEqual(0, 1, "点击footballFail")
        else:
            with self.subTest(data="点击footballPASS"):
                self.assertEqual(0, 0, "点击footballPASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_host_name_title"]').set_text("测试1")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="主队输入Fail"):
                self.assertEqual(0, 1, "主队输入Fail")
        else:
            with self.subTest(data="主队输入PASS"):
                self.assertEqual(0, 0, "主队输入PASS")

        '''
                try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_host_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击host_nameFail"):
                self.assertEqual(0, 1, "点击host_nameFail")
        else:
            with self.subTest(data="点击host_namePASS"):
                self.assertEqual(0, 0, "点击host_namePASS")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击playteam1Fail"):
                self.assertEqual(0, 1, "点击playteam1Fail")
        else:
            with self.subTest(data="点击playteam1PASS"):
                self.assertEqual(0, 0, "点击playteam1PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteam Fail"):
                self.assertEqual(0, 1, "点击guestteam Fail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        '''
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_guest_name_title"]').click()
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_guest_name_title"]').set_text("测试2")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="客队输入Fail"):
                self.assertEqual(0, 1, "客队输入Fail")
        else:
            with self.subTest(data="客队输入PASS"):
                self.assertEqual(0, 0, "客队输入PASS")
        '''
                try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_guest_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="guest_name select Fail"):
                self.assertEqual(0, 1, "点击guest_name Fail")
        else:
            with self.subTest(data="guest_name select pass"):
                self.assertEqual(0, 0, "点击guest_name pass")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击exitteam Fail"):
                self.assertEqual(0, 1, "点击exitteam Fail")
        else:
            with self.subTest(data="点击exitteam PASS"):
                self.assertEqual(0, 0, "点击exitteam PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteamFail"):
                self.assertEqual(0, 1, "点击guestteamFail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        '''

        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_start_time_rl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击starttime Fail"):
                self.assertEqual(0, 1, "点击starttime Fail")
        else:
            with self.subTest(data="点击starttime PASS"):
                self.assertEqual(0, 0, "点击starttime PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/btn_sure"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击timesure Fail"):
                self.assertEqual(0, 1, "点击timesure Fail")
        else:
            with self.subTest(data="点击timesure PASS"):
                self.assertEqual(0, 0, "点击timesure PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_place"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placeFail"):
                self.assertEqual(0, 1, "点击placeFail")
        else:
            with self.subTest(data="点击place PASS"):
                self.assertEqual(0, 0, "点击place PASS")


        try:
            d.swipe(0, 1491, 0, 1634, 0.5)  # 滑动选择153测试站点，for 0.5s(default)
            time.sleep(2)
            #d.xpath('//*[@text="153测试"]')
            s1=d.xpath('//*[@text="153测试"]').get_text()
            if s1=="153测试":
                with self.subTest(data="滑动选择153测试站点 pass"):
                    self.assertEqual(0, 0, "滑动选择153测试站点 pass")
            else:
                with self.subTest(data="滑动选择153测试站点 fail"):
                    self.assertEqual(0, 1, "滑动选择153测试站点 fail")
        except Exception as e:
            with self.subTest(data="滑动选择153测试站点 Fail"):
                self.assertEqual(0, 1, "滑动选择153测试站点 Fail")
        else:
            with self.subTest(data="滑动选择153测试站点 PASS"):
                self.assertEqual(0, 0, "滑动选择153测试站点 PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_type_confirm"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placesure Fail"):
                self.assertEqual(0, 1, "点击placesure Fail")
        else:
            with self.subTest(data="点击placesure PASS"):
                self.assertEqual(0, 0, "点击placesure PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballsure Fail"):
                self.assertEqual(0, 1, "点击footballsure Fail")
        else:
            with self.subTest(data="点击footballsure PASS"):
                self.assertEqual(0, 0, "点击footballsure PASS")
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")
    def test_1_app_createfootball_3_selectteam(self):
        """新增球队界面输入主队"""
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
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/main_create_race"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击创建活动Fail"):
                self.assertEqual(0, 1, "点击创建活动Fail")
        else:
            with self.subTest(data="点击创建活动PASS"):
                self.assertEqual(0, 0, "点击创建活动PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_create_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballFail"):
                self.assertEqual(0, 1, "点击footballFail")
        else:
            with self.subTest(data="点击footballPASS"):
                self.assertEqual(0, 0, "点击footballPASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_host_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击host_nameFail"):
                self.assertEqual(0, 1, "点击host_nameFail")
        else:
            with self.subTest(data="点击host_namePASS"):
                self.assertEqual(0, 0, "点击host_namePASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_fill_team_name"]').set_text("test1")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入主队名称Fail"):
                self.assertEqual(0, 1, "输入主队名称Fail")
        else:
            with self.subTest(data="输入主队名称PASS"):
                self.assertEqual(0, 0, "输入主队名称PASS")

        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_team_brief_name_et"]').click()
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_team_brief_name_et"]').set_text("test1")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="主队简称输入 Fail"):
                self.assertEqual(0, 1, "主队简称输入Fail")
        else:
            with self.subTest(data="主队简称输入PASS"):
                self.assertEqual(0, 0, "主队简称输入PASS")
        try:
            d.click(0.881, 0.969)
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="输入法切换 Fail"):
                self.assertEqual(0, 1, "输入法切换Fail")
        else:
            with self.subTest(data="输入法切换PASS"):
                self.assertEqual(0, 0, "输入法切换PASS")
        try:
            d.click(0.932, 0.815)
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="选择华为输入法 Fail"):
                self.assertEqual(0, 1, "选择华为输入法Fail")
        else:
            with self.subTest(data="选择华为输入法PASS"):
                self.assertEqual(0, 0, "选择华为输入法PASS")
        try:
            d(resourceId="android:id/fullscreenArea").exists()
            time.sleep(4)
            d.click(0.933, 0.617)
        except Exception as e:
            pass
        else:
            pass
        try:
            d.click(0.935, 0.619)
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="隐藏输入法使确定按钮显示出来 Fail"):
                self.assertEqual(0, 1, "隐藏输入法使确定按钮显示出来Fail")
        else:
            with self.subTest(data="隐藏输入法使确定按钮显示出来PASS"):
                self.assertEqual(0, 0, "隐藏输入法使确定按钮显示出来PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="主队创建新球队 Fail"):
                self.assertEqual(0, 1, "主队创建新球队Fail")
        else:
            with self.subTest(data="主队创建新球队PASS"):
                self.assertEqual(0, 0, "主队创建新球队PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_guest_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="guest_name select Fail"):
                self.assertEqual(0, 1, "点击guest_name Fail")
        else:
            with self.subTest(data="guest_name select pass"):
                self.assertEqual(0, 0, "点击guest_name pass")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击exitteam Fail"):
                self.assertEqual(0, 1, "点击exitteam Fail")
        else:
            with self.subTest(data="点击exitteam PASS"):
                self.assertEqual(0, 0, "点击exitteam PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteamFail"):
                self.assertEqual(0, 1, "点击guestteamFail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_start_time_rl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击starttime Fail"):
                self.assertEqual(0, 1, "点击starttime Fail")
        else:
            with self.subTest(data="点击starttime PASS"):
                self.assertEqual(0, 0, "点击starttime PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/btn_sure"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击timesure Fail"):
                self.assertEqual(0, 1, "点击timesure Fail")
        else:
            with self.subTest(data="点击timesure PASS"):
                self.assertEqual(0, 0, "点击timesure PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_place"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placeFail"):
                self.assertEqual(0, 1, "点击placeFail")
        else:
            with self.subTest(data="点击place PASS"):
                self.assertEqual(0, 0, "点击place PASS")


        try:
            d.swipe(0, 1491, 0, 1634, 0.5)  # 滑动选择153测试站点，for 0.5s(default)
            time.sleep(2)
            #d.xpath('//*[@text="153测试"]')
            s1=d.xpath('//*[@text="153测试"]').get_text()
            if s1=="153测试":
                with self.subTest(data="滑动选择153测试站点 pass"):
                    self.assertEqual(0, 0, "滑动选择153测试站点 pass")
            else:
                with self.subTest(data="滑动选择153测试站点 fail"):
                    self.assertEqual(0, 1, "滑动选择153测试站点 fail")
        except Exception as e:
            with self.subTest(data="滑动选择153测试站点 Fail"):
                self.assertEqual(0, 1, "滑动选择153测试站点 Fail")
        else:
            with self.subTest(data="滑动选择153测试站点 PASS"):
                self.assertEqual(0, 0, "滑动选择153测试站点 PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_type_confirm"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placesure Fail"):
                self.assertEqual(0, 1, "点击placesure Fail")
        else:
            with self.subTest(data="点击placesure PASS"):
                self.assertEqual(0, 0, "点击placesure PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballsure Fail"):
                self.assertEqual(0, 1, "点击footballsure Fail")
        else:
            with self.subTest(data="点击footballsure PASS"):
                self.assertEqual(0, 0, "点击footballsure PASS")
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")
    def test_1_app_createfootball_4_selectteam(self):
        """新增球队界面输入客队"""
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
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/main_create_race"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击创建活动Fail"):
                self.assertEqual(0, 1, "点击创建活动Fail")
        else:
            with self.subTest(data="点击创建活动PASS"):
                self.assertEqual(0, 0, "点击创建活动PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/ht_create_gird"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballFail"):
                self.assertEqual(0, 1, "点击footballFail")
        else:
            with self.subTest(data="点击footballPASS"):
                self.assertEqual(0, 0, "点击footballPASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_guest_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击host_nameFail"):
                self.assertEqual(0, 1, "点击host_nameFail")
        else:
            with self.subTest(data="点击host_namePASS"):
                self.assertEqual(0, 0, "点击host_namePASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_fill_team_name"]').set_text("test1")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入主队名称Fail"):
                self.assertEqual(0, 1, "输入主队名称Fail")
        else:
            with self.subTest(data="输入主队名称PASS"):
                self.assertEqual(0, 0, "输入主队名称PASS")

        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_team_brief_name_et"]').click()
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_team_brief_name_et"]').set_text("test1")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="主队简称输入 Fail"):
                self.assertEqual(0, 1, "主队简称输入Fail")
        else:
            with self.subTest(data="主队简称输入PASS"):
                self.assertEqual(0, 0, "主队简称输入PASS")
        try:
            d.click(0.881, 0.969)
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="输入法切换 Fail"):
                self.assertEqual(0, 1, "输入法切换Fail")
        else:
            with self.subTest(data="输入法切换PASS"):
                self.assertEqual(0, 0, "输入法切换PASS")
        try:
            d.click(0.932, 0.815)
            time.sleep(4)
        except Exception as e:
            with self.subTest(data="选择华为输入法 Fail"):
                self.assertEqual(0, 1, "选择华为输入法Fail")
        else:
            with self.subTest(data="选择华为输入法PASS"):
                self.assertEqual(0, 0, "选择华为输入法PASS")
        try:
            d(resourceId="android:id/fullscreenArea").exists()
            time.sleep(4)
            d.click(0.933, 0.617)
        except Exception as e:
            pass
        else:
            pass

        try:
            d.click(0.935, 0.619)
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="隐藏输入法使确定按钮显示出来 Fail"):
                self.assertEqual(0, 1, "隐藏输入法使确定按钮显示出来Fail")
        else:
            with self.subTest(data="隐藏输入法使确定按钮显示出来PASS"):
                self.assertEqual(0, 0, "隐藏输入法使确定按钮显示出来PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="主队创建新球队 Fail"):
                self.assertEqual(0, 1, "主队创建新球队Fail")
        else:
            with self.subTest(data="主队创建新球队PASS"):
                self.assertEqual(0, 0, "主队创建新球队PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_select_host_name"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="guest_name select Fail"):
                self.assertEqual(0, 1, "点击guest_name Fail")
        else:
            with self.subTest(data="guest_name select pass"):
                self.assertEqual(0, 0, "点击guest_name pass")
        try:
            d.xpath('//*[@text="选择已存在球队"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击exitteam Fail"):
                self.assertEqual(0, 1, "点击exitteam Fail")
        else:
            with self.subTest(data="点击exitteam PASS"):
                self.assertEqual(0, 0, "点击exitteam PASS")
        try:
            d.xpath(
                '//*[@resource-id="com.huiti.score:id/mListView"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击guestteamFail"):
                self.assertEqual(0, 1, "点击guestteamFail")
        else:
            with self.subTest(data="点击guestteam PASS"):
                self.assertEqual(0, 0, "点击guestteam PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_start_time_rl"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击starttime Fail"):
                self.assertEqual(0, 1, "点击starttime Fail")
        else:
            with self.subTest(data="点击starttime PASS"):
                self.assertEqual(0, 0, "点击starttime PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/btn_sure"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击timesure Fail"):
                self.assertEqual(0, 1, "点击timesure Fail")
        else:
            with self.subTest(data="点击timesure PASS"):
                self.assertEqual(0, 0, "点击timesure PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_school_place"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placeFail"):
                self.assertEqual(0, 1, "点击placeFail")
        else:
            with self.subTest(data="点击place PASS"):
                self.assertEqual(0, 0, "点击place PASS")


        try:
            d.swipe(0, 1491, 0, 1634, 0.5)  # 滑动选择153测试站点，for 0.5s(default)
            time.sleep(2)
            #d.xpath('//*[@text="153测试"]')
            s1=d.xpath('//*[@text="153测试"]').get_text()
            if s1=="153测试":
                with self.subTest(data="滑动选择153测试站点 pass"):
                    self.assertEqual(0, 0, "滑动选择153测试站点 pass")
            else:
                with self.subTest(data="滑动选择153测试站点 fail"):
                    self.assertEqual(0, 1, "滑动选择153测试站点 fail")
        except Exception as e:
            with self.subTest(data="滑动选择153测试站点 Fail"):
                self.assertEqual(0, 1, "滑动选择153测试站点 Fail")
        else:
            with self.subTest(data="滑动选择153测试站点 PASS"):
                self.assertEqual(0, 0, "滑动选择153测试站点 PASS")
        try:
            d.xpath('//*[@resource-id="com.huiti.score:id/ht_match_type_confirm"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击placesure Fail"):
                self.assertEqual(0, 1, "点击placesure Fail")
        else:
            with self.subTest(data="点击placesure PASS"):
                self.assertEqual(0, 0, "点击placesure PASS")
        try:
            d.xpath('//*[@text="确定"]').click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击footballsure Fail"):
                self.assertEqual(0, 1, "点击footballsure Fail")
        else:
            with self.subTest(data="点击footballsure PASS"):
                self.assertEqual(0, 0, "点击footballsure PASS")
        try:
            d.app_stop("com.huiti.score")
        except Exception as e:
            with self.subTest(data="点击appstop Fail"):
                self.assertEqual(0, 1, "点击appstop Fail")
        else:
            with self.subTest(data="点击appstop PASS"):
                self.assertEqual(0, 0, "点击appstop PASS")




