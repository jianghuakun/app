from selenium import webdriver
import time
url="https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ee9a61a8a93d49adb31e5417e3cf84a7"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(10)
driver.find_element_by_xpath("//li[@id='ttbar-login' and @class='shortcut_btn fore1 dropdown']/a[@class='link-login']").click()
driver.find_element_by_xpath("//div[@class='login-tab login-tab-r']/a[@href='javascript:void(0)']").click()
driver.find_element_by_xpath("//input[@id='loginname']").click()
driver.find_element_by_xpath("//input[@id='loginname']").send_keys("13691699127")
driver.find_element_by_xpath("//input[@id='nloginpwd']").click()
driver.find_element_by_xpath("//input[@id='nloginpwd']").send_keys("hupu1020")
driver.find_element_by_xpath("//a[@id='loginsubmit' and @class='btn-img btn-entry']").click()

