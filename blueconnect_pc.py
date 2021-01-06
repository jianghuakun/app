import sounddevice as sd
dev=sd.query_devices()
#print(dev)
import sys
import os

from PIL import ImageGrab
from aip import AipOcr
import time
from selenium import webdriver
from PIL import ImageGrab
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#PC机连接耳机，然后通过连接还是断开进行判断

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
flag=True
tic = time.clock()
count1 = 0
count2 = 0
while flag:
    time.sleep(60)
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.quit()
    bbox = (700, 500, 1000, 730)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    im.save('as.png')
    # data = json_decode(self.request.body)
    """ 你的 APPID AK SK """
    APP_ID = '17542401'
    API_KEY = 'FAs0yQLEfaL9i14nbKVATWT1'
    SECRET_KEY = 'mYuqi3iXpur1K6ypR3dKzTFroq2LKe7D '
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    for i in range(1, 2):
        """ 读取图片 """


        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()


        image = get_file_content(r'D:\python\python36-64\project\app\as.png')
        """ 调用通用文字识别（含位置高精度版） """
        result=client.general(image)
        """ 如果有可选参数 """
        options = {}
        options["recognize_granularity"] = "big"
        options["detect_direction"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"
        """  带参数调用通用文字识别（含位置高精度版）   """
        #result = client.accurate(image, options)

        '''
        url = "http//www.x.com/sample.jpg"

        """ 调用通用文字识别, 图片参数为远程url图片 """
        client.generalUrl(url);

        """ 如果有可选参数 """
        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"
        """ 带参数调用通用文字识别, 图片参数为远程url图片 """
        client.generalUrl(url, options)
        '''

        try:
            list1 = result["words_result"]
            for x1 in list1:
                print(x1)
                toc = time.clock()
                tt = "测试时间: " + "%.2f" % (toc - tic) + " s"
                print(tt)
                if x1["words"] == r"已配对" or float("%.2f" % (toc - tic)) / 60/60 > 20.0:
                    print(count1)
                    im = ImageGrab.grab()

                    #starttime = time.strftime("%Y%m%d", time.localtime())
                    starttime=time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
                    im.save('D:\性能测试-%s.png'% starttime)
                    count1+=1
                    if count1>10:
                        flag = False
                    else:
                        pass
                elif x1["words"]==r"已连接语音,音乐":

                    count1=0
                    print(count1)
                else:
                    print("12")
                    print(x1["words"])

        except:
            pass



