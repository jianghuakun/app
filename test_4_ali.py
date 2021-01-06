from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
class ali(unittest.TestCase):
    def setUp(self):
        print("阿里云测试开始")

    def test_1_selenium_1_video(self):
        url = "https://www.aliyun.com/"
        driver = webdriver.Chrome()
        # 设置窗口最大化
        driver.maximize_window()
        # 访问被测网页
        driver.get(url)
        time.sleep(10)

        #cur_handles = driver.window_handles
        #点击控制台
        try:
            login_p = driver.find_elements_by_xpath(
                "//div[@class='aliyun-topbar-element aliyun-ability-topbar']/a[@class='ace-link ace-link-primary ability-element-topbar']")
            login_p[3].click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="点击控制台Fail"):
                self.assertEqual(0, 1, "点击控制台Fail")
        else:
            with self.subTest(data="点击控制台PASS"):
                self.assertEqual(0, 0, "点击控制台PASS")
        #WebDriverWait(driver, 20).until(EC.new_window_is_opened(cur_handles))
        time.sleep(2)
        ifames=driver.find_elements_by_xpath("//iframe")
        for x in ifames:
            print(x.get_attribute("id"))
            with self.subTest(data=x.get_attribute("id")):
                self.assertEqual(x.get_attribute("id"), 1, "账户密码登录存在Fail")
        time.sleep(2)
        driver.switch_to.frame(ifames[1])
        #driver.switch_to.frame('alibaba-login-box')
        try:
            driver.find_element_by_xpath(
                "//div[@class='ability-tabs-item ' and @data-tracker-name='账号密码登录' and @data-spm-click='gostr=/aliyun;locaid=login']").click()
            time.sleep(2)
            #driver.find_element_by_xpath("//div[@class='input-plain-wrap input-wrap-password']/input[@id='fm-login-id']").send_keys("jianghuakun1234")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="账户密码登录存在不存在"):
                self.assertEqual(0, 1, "账户密码登录存在Fail")
        else:
            with self.subTest(data="账户密码登录存在"):
                self.assertEqual(0, 0, "输入用户名PASS")
        try:
            s1=driver.find_element_by_xpath(
                "//div[@class='input-plain-wrap input-wrap-loginid ']/input[@id='fm-login-id' and @class='fm-text' and @name='fm-login-id']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='input-plain-wrap input-wrap-loginid ']/input[@id='fm-login-id' and @class='fm-text' and @name='fm-login-id']").send_keys("jianghuakun1234")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入用户名Fail"):
                self.assertEqual(0, 1, "输入用户名Fail")
        else:
            with self.subTest(data="输入用户名Pass"):
                self.assertEqual(0, 0, "输入用户名PASS")
        #输入密码
        try:
            driver.find_element_by_xpath(
                "//div[@class='input-plain-wrap input-wrap-password']/input[@id='fm-login-password']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//div[@class='input-plain-wrap input-wrap-password']/input[@id='fm-login-password']").send_keys("hupu1020")
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="输入密码Fail"):
                self.assertEqual(0, 1, "输入密码Fail")
        else:
            with self.subTest(data="输入密码PASS"):
                self.assertEqual(0, 0, "输入密码PASS")


