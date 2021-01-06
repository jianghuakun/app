# coding=utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
time.sleep(3)
element = driver.find_element_by_tag_name("body")
element.send_keys(Keys.CONTROL,Keys.SHIFT,'i')
#driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL+Keys.SHIFT+'i')
time.sleep(3)



# 定位元素
ele_1 = driver.find_element_by_xpath("//div[@class='s-bottom-layer-left']/p[@class='lh']/a[@class='c-color-gray2' and @href='//home.baidu.com']")
ele_2 = driver.find_element_by_xpath("//div[@class='s-bottom-layer-left']/p[@class='lh']/a[@class='c-color-gray2' and @href='http://e.baidu.com/?refer=888']")

# 将鼠标悬停在元素1上3秒后再次悬停到元素2上
ActionChains(driver).move_to_element(ele_1).perform()
time.sleep(3)
ActionChains(driver).move_to_element(ele_2).perform()
time.sleep(3)

driver.quit()