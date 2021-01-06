#usr/bin/python3
from selenium import webdriver
import time
import unittest
class test_2_web_ui2(unittest.TestCase):
    """视频网站登录"""
    def setUp(self):
        print("视频网站测试开始")

    def test_1_selenium_1_video(self):
        url = "http://home.xiaoqiu.tv/#/videomore?navType=hotVideoGroup&groupName=%E7%83%AD%E9%97%A8"
        driver = webdriver.Chrome()
        # 设置窗口最大化
        driver.maximize_window()
        # 访问被测网页
        driver.get(url)
        time.sleep(10)
        #logo判断
        #首页判断
        try:
            index = driver.find_elements_by_xpath("//nav[@class='videoindexwidth']/div[@class='nav-itembox']/span[@onclick='location.replace('#/')']").click()
            time.sleep(2)
            with self.subTest(data="视频模块判断"):
                self.assertEqual(len(index), 4, "视频模块判断")
            homepage=index[0].text
            remen=index[1].text
            gongkai=index[2].text
            xiaoyuan = index[3].text
            if homepage=="首页":
                with self.subTest(data="首页判断"):
                    self.assertEqual(homepage, "首页", "首页判断PASS")
                try:
                    indexpage=index[0].click()
                    time.sleep(2)
                except Exception as e:
                    with self.subTest(data="切换首页Fail"):
                        self.assertEqual(0, 1, "切换首页Fail")
                else:
                    with self.subTest(data="切换首页pass"):
                        self.assertEqual(0, 0, "切换首页pass")
                    try:
                        newvideo1=driver.find_elements_by_xpath("//div[@class='greatvideo']/div[@class='videoindextitle']")
                        if newvideo1[0].text=="最新视频":
                            with self.subTest(data="最新视频标题pass"):
                                self.assertEqual(newvideo1[0].text, "最新视频", "最新视频标题pass")
                            driver.get_screenshot_as_file("D:/app/最新视频标题pass.png")
                        else:
                            with self.subTest(data="最新视频标题fail"):
                                self.assertEqual(newvideo1[0].text, "最新视频", "最新视频标题fail")
                            driver.get_screenshot_as_file("D:/app/最新视频标题fail.png")
                        time.sleep(2)
                    except Exception as e:
                        with self.subTest(data="最新视频页Fail"):
                            self.assertEqual(0, 1, "最新视频Fail")
                        driver.get_screenshot_as_file("D:/app/最新视频标题异常.png")
                    else:
                        pass
                    try:
                        hotvideo=driver.find_elements_by_xpath("//div[@class='videoflexitem ']/div[@class='headtitle']/span")
                        if hotvideo[0].text=="热门视频":
                            with self.subTest(data="热门视频标题pass"):
                                self.assertEqual(hotvideo[0].text, "热门视频", "热门视频标题pass")
                            driver.get_screenshot_as_file("D:/app/热门视频标题pass.png")
                        else:
                            with self.subTest(data="热门视频标题fail"):
                                self.assertEqual(hotvideo[0].text, "热门视频", "热门视频标题fail")
                            driver.get_screenshot_as_file("D:/app/热门视频标题fail.png")
                        time.sleep(2)
                    except Exception as e:
                        with self.subTest(data="热门视频页Fail"):
                            self.assertEqual(0, 1, "热门视频Fail")
                        driver.get_screenshot_as_file("D:/app/热门视频标题异常.png")
                    else:
                        pass


            else:
                with self.subTest(data="首页判断"):
                    self.assertEqual(homepage, "首页", "首页判断fail")
            time.sleep(1)
            if remen=="热门":
                with self.subTest(data="热门"):
                    self.assertEqual(remen, "热门", "热门判断成功")
            else:
                with self.subTest(data="热门"):
                    self.assertEqual(remen, "热门", "热门判断失败")
            time.sleep(1)
            if gongkai=="公开":
                with self.subTest(data="公开"):
                    self.assertEqual(gongkai, "公开", "公开判断成功")
            else:
                with self.subTest(data="公开"):
                    self.assertEqual(gongkai, "公开", "公开判断失败")
            time.sleep(1)
            if xiaoyuan=="校园":
                with self.subTest(data="校园"):
                    self.assertEqual(xiaoyuan, "校园", "校园判断成功")
            else:
                with self.subTest(data="校园"):
                    self.assertEqual(xiaoyuan, "校园", "校园判断失败")
            time.sleep(1)
        except Exception as e:
            with self.subTest(data="index异常"):
                self.assertEqual(0, 1, "index异常")
        else:
            pass
        # div=driver.find_elements_by_class_name("videoitem hvr-underline-from-center")
        div = driver.find_elements_by_xpath(
            "//div[@class='videobox ']/div[@class='videoitem hvr-underline-from-center']")

        print(len(div))
        for i in div:
            imgs = i.find_elements_by_xpath("div[@class='titlebox']/div[@class='videotitle']")
            # img=imgs[0].text
            print(imgs[0].text, type(imgs))
        # 点击登录，弹出登录弹框
        login = driver.find_element_by_xpath("//div[@class='logout']").click()

        # 弹框处理
        driver.find_element_by_xpath("//div[@class='input ']/input[@placeholder='请输入登录名']").click()
        time.sleep(2)

        #用户名和密码正确
        try:
            driver.find_element_by_xpath("//div[@class='input ']/input[@placeholder='请输入登录名']").send_keys("jianghuakun")
            time.sleep(2)
            driver.find_element_by_xpath("//input[@placeholder='请输入密码']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("123456")
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='loginbutton']").click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="登录失败"):
                self.assertEqual(0, 1, "登录失败")
        else:
            with self.subTest(data="登录成功"):
                self.assertEqual(0, 0, "登录成功")
        #用户名为空
        try:
            driver.find_element_by_xpath("//div[@class='input ']/input[@placeholder='请输入登录名']").send_keys("")
            time.sleep(2)
            driver.find_element_by_xpath("//input[@placeholder='请输入密码']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("123456")
            time.sleep(2)
            driver.find_element_by_xpath("//div[@class='loginbutton']").click()
            time.sleep(2)
        except Exception as e:
            print("用户名密码错误")
            with self.subTest(data="用户名密码错误测试通过"):
                self.assertEqual(1, 1, "用户名密码错误测试通过")
        else:
            print("登录成功")
            with self.subTest(data="用户名密码错误测试失败"):
                self.assertEqual(0, 1, "用户名密码错误测试失败")

        # d.xpath('//*[@text="智慧校园运动场"]').click()
        time.sleep(1)
        driver.quit()
    def test_2_selenium_1_gz(self):
        url = "http://gz.fenda.com/"
        driver = webdriver.Chrome()
        # 设置窗口最大化
        driver.maximize_window()
        # 访问被测网页
        driver.get(url)
        time.sleep(10)

        #用户名密码正确
        try:
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").send_keys("040396")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").send_keys(
                "hupu1020")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='text-align :left ']/input[@id='btnLogIn']").click()
            time.sleep(2)
            #登录成功后界面测试1
            #driver.switch_to.frame('boardtitle')
            # 登录成功后界面测试2
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            #1.用户名判断
            s1=driver.find_elements_by_xpath("//span")
            with self.subTest(data=s1[0].text):
                self.assertEqual(s1[0].text, "查询工资", "ifram切换")
            with self.subTest(data=s1[1].text):
                self.assertEqual(s1[1].text, "人事查询", "ifram切换")
            with self.subTest(data=s1[2].text):
                self.assertEqual(s1[2].text, "修改密码", "修改密码")
            with self.subTest(data=s1[3].text):
                self.assertEqual(s1[3].text, "系统使用说明", "系统使用说明")
            with self.subTest(data=s1[4].text):
                self.assertEqual(s1[4].text, "安全退出", "安全退出")
            driver.switch_to.parent_frame()  #后退
            driver.switch_to.frame('mainframe')
            #iframe = driver.find_elements_by_xpath("//iframe")
            key=driver.find_elements_by_xpath("//tbody/tr")
            key1=key[0].find_elements_by_xpath("th")
            value1=key[2].find_elements_by_xpath("td")
            list1=[]
            for i in range(0,len(key1)):


                if key1[i].text=="伙食信息":
                    key2=key[1].find_elements_by_xpath("th")
                    for j in range(0,3):
                        list2={key2[j].text:value1[i+j].text}
                        list1.append(list2)

                elif key1[i].text=="专项扣除信息":
                    key2 = key[1].find_elements_by_xpath("th")
                    for k in range(0, 6):
                        list2 = {key2[3+k].text: value1[i +2+ k].text}
                        list1.append(list2)
                elif i>=24 and i<33:
                    list2 = {key1[i].text: value1[i+2].text}
                    list1.append(list2)
                else:
                    list2 = {key1[i].text: value1[i].text}
                    list1.append(list2)
            with self.subTest(data=list1):
                self.assertEqual(len(list1), "安全退出", "安全退出")


            '''
           cxgz=driver.find_element_by_xpath("//tbody/tr/td/div/a[@href='gzcx.aspx']/span").text
            with self.subTest(data="gzlogin"):
                self.assertEqual(cxgz, "查询工资", "查询工资文案正确") 
            '''

        except Exception as e:
            with self.subTest(data="用户名密码正确登录失败"):
                self.assertEqual(0, 1, "用户名密码正确登录失败")
        else:
            with self.subTest(data="用户名密码正确登录成功"):
                self.assertEqual(0, 0, "用户名密码正确登录成功")
        #用户名不正确，密码正确
        try:
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").send_keys(
                "40396")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").click()
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").send_keys(
                "hupu1020")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='text-align :left ']/input[@id='btnLogIn']").click()
            time.sleep(2)
            body=driver.find_elements_by_xpath("//span[@style='font-size: medium; font-weight: 700;']")
            with self.subTest(data=body):
                self.assertEqual(body, 1, "用户名错误测试通过")

        except Exception as e:
            print("用户名密码错误")
            with self.subTest(data="用户名错误测试通过"):
                self.assertEqual(1, 1, "用户名错误测试通过")
        else:
            print("登录成功")
            with self.subTest(data="用户名错误测试失败"):
                self.assertEqual(0, 1, "用户名错误测试失败")
        #用户名正确，密码不正确
        try:
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbUserName']").send_keys("040396")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='height :35px; text-align :left']/input[@id='tbPassword']").send_keys(
                "hupu1021")
            time.sleep(2)
            driver.find_element_by_xpath(
                "//tbody/tr/td[@style='text-align :left ']/input[@id='btnLogIn']").click()
            time.sleep(2)
        except Exception as e:
            with self.subTest(data="密码错误测试通过"):
                self.assertEqual(1, 1, "密码错误测试通过")
        else:
            with self.subTest(data="密码错误测试失败"):
                self.assertEqual(1, 0, "密码错误测试失败")

        # d.xpath('//*[@text="智慧校园运动场"]').click()
        time.sleep(1)
        driver.quit()
