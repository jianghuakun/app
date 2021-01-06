from selenium import webdriver
import time
#定义被测网页
url1 = "https://list.jd.com/list.html?cat=652,828,842&ev=2895%5F117843&sort=sort_totalsales15_desc&trans=1&JL=3_%E4%BD%A9%E6%88%B4%E6%96%B9%E5%BC%8F_%E7%9C%9F%E6%97%A0%E7%BA%BF#J_crumbsBar"
#获取浏览器操作对象
driver = webdriver.Chrome()
#设置窗口最大化
driver.maximize_window()
#访问被测网页
driver.get(url1)
#通过id查找输入框并清空输入框
driver.find_element_by_id('kw').clear()
#在输入框中输入'selenium'
driver.find_element_by_id('kw').send_keys('python3')
time.sleep(1)
#通过id查询'百度一下'按钮，并触发点击事件
driver.find_element_by_id('su').click()
#打印title
print(driver.title,"by_id")
#等待1s， 并退出浏览器
time.sleep(1)
driver.quit()

from selenium import webdriver
import time
#定义被测网页
url1 = "https://www.baidu.com/"
#获取浏览器操作对象
driver = webdriver.Chrome()
#设置窗口最大化
driver.maximize_window()
#访问被测网页
driver.get(url1)
#通过name查找输入框并清空输入框
driver.find_element_by_name('wd').clear()
#在输入框中输入'selenium'
driver.find_element_by_name('wd').send_keys('selenium3')
time.sleep(1)
#通过name查询'百度一下'按钮，并触发点击事件,因为'百度一下'按钮没有提供name属性，所以次处不能通过name定位
driver.find_element_by_id('su').click()
#打印title
print(driver.title,"by_name")
#等待1s， 并退出浏览器
time.sleep(1)
driver.quit()