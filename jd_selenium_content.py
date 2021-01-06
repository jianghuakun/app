
from selenium import webdriver
from urllib.parse import quote
import time
import random
driver = webdriver.Chrome()  # 打开浏览器
driver.maximize_window()
key = '红酒'  # 设置搜索商品关键词
url = 'https://search.jd.com/Search?keyword=' + quote(key) + '&enc=utf-8'  # 构造url
driver.get(url)  # 打开url
driver.implicitly_wait(3)  # 等待
links = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a')  # 查找当前页面的商品链接
urls = [l.get_attribute('href') for l in links]
#url = urls[1]  # 获取第一个商品链接
url="https://item.jd.com/100004325476.html"
driver.get(url)  # 打开页面
driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()  # 点击商品评论
# 获取评论数据
#ss=driver.find_element_by_xpath('//*[@div="ui-page"]/a[@class="ui-pager-next"]').click()  # 点击下一页评论
flag=True
count=0
while flag:
    count+=1
    t1=random.randrange(1,5)
    time.sleep(t1)
    try:
        comment_list = driver.find_elements_by_xpath('//*[@id="comment-0"]//div/div[2]/p')
        comment_text_list = [c.text for c in comment_list]
        print(comment_text_list)
        text=driver.find_element_by_link_text('下一页').get_attribute("href")
        if text=="#comment":
            text = driver.find_element_by_link_text('下一页').click()
        elif text=="#askAnswer":
            flag=False
    except:
        print("下一页不存在")
        flag=False

print(count)
driver.close()


