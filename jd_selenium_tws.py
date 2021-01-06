from selenium import webdriver
import time
import requests
from config.mysql_87 import mysql_87
count=0
for i in range(1,66):
    url1="https://list.jd.com/list.html?cat=652,828,842&ev=2895%5F117843&page="+str(i)+"&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    #url1 = "https://list.jd.com/list.html?cat=652,828,842&ev=2895%5F117843&sort=sort_totalsales15_desc&trans=1&JL=3_%E4%BD%A9%E6%88%B4%E6%96%B9%E5%BC%8F_%E7%9C%9F%E6%97%A0%E7%BA%BF#J_crumbsBar"
    # 获取浏览器操作对象
    driver = webdriver.Chrome()
    # 设置窗口最大化
    driver.maximize_window()
    # 访问被测网页
    driver.get(url1)
    time.sleep(10)
    div = driver.find_elements_by_class_name("gl-item")

    for x in div:
        x1 = x.find_element_by_xpath("div/div[@class='p-img']/a")
        url = x1.get_attribute("href")
        x2 = x.find_element_by_xpath("div/div[@class='p-price']/strong[@class='J_price']/i")
        price = x2.text
        x3 = x.find_element_by_xpath("div/div[@class='p-name']/a")
        name = x3.get_attribute("title")
        print(url, price, name)
        # print(x1[0].get_attribute("href"))
        count += 1
        list1={"url":url,"price":price,"name":name}
        mysql_87.test1_cursor.execute("insert into tws(`url`,`price`,`name`) values(%s,%s,%s)",[list1["url"],list1["price"],list1["name"]])
        mysql_87.test1.commit()
    driver.quit()

print(count)
time.sleep(1)
