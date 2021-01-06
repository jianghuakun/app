#usr/bin/python3
from selenium import webdriver
import time
import unittest
from config.redis245 import redis245
for i in range(0,1):
    url = "http://192.168.75.245:9020/user/login?redirect=%2Fiversion%2Fupdate"
    driver = webdriver.Chrome()
    # 设置窗口最大化
    driver.maximize_window()
    # 访问被测网页
    driver.get(url)
    title = driver.title
    #time.sleep(60)
    #time.sleep(30)
    driver.find_element_by_xpath('//input[@placeholder="请输入帐户名"]').click()
    driver.find_element_by_xpath('//input[@placeholder="请输入帐户名"]').send_keys("jianghuakun")
    driver.find_element_by_xpath('//input[@placeholder="请输入帐户名"]').is_displayed()
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').click()
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("123456")

    driver.find_element_by_xpath('//button[@type="submit"]').click()
    s1 = redis245.Cluster
    captchas = s1.keys("*")
    for captcha1 in captchas:
        if ":" not in captcha1 and len(captcha1) == 32:
            captcha = s1.get(captcha1).replace('"', '').lower()
            driver.find_element_by_xpath('//input[@placeholder="请输入验证码"]').click()
            driver.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys(captcha)
            current_window = driver.current_window_handle  # 获取当前窗口handle name
            driver.find_element_by_xpath('//button[@type="submit"]').click()
            title1 = driver.title
            all_window = driver.window_handles
            for window in all_window:
                if window != current_window:
                    driver.switch_to.window(window)
            current_window = driver.current_window_handle
            #driver.switch_to.window(driver.window_handles[0])
            #text1=driver.find_element_by_xpath('//body/div[@id="app"]')
            time.sleep(30)
            #text2=driver.find_element_by_css_selector("section.layout.ant-layout.ant-layout-has-sider.desktop")
            text2 = driver.find_element_by_xpath('//body/div[@id="app"]/section[@class="layout ant-layout ant-layout-has-sider desktop"]').is_displayed()
            text3=driver.find_elements_by_xpath('//span[@class="action action-full ant-dropdown-link user-dropdown-menu ant-dropdown-trigger"]')
            print(text2,text3,title,title1)

    time.sleep(30)
    #driver.quit()

