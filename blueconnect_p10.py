
import time
from selenium import webdriver
import uiautomator2 as u2
import os
#PC机连接耳机，然后通过连接还是断开进行判断

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
flag=True
tic = time.clock()
phonelist={"华为P10":"VTR-AL00","华为Mate20":"LYA-AL00","三星Note10":"SM-N9700"}
ss=input("请选择手机型号：1：华为P10，型号：VTR-AL00；2：华为Mate20；型号：LYA-AL00；3：三星Note10，型号：SM-N9700  ")
if ss=="1":
    print("你的测试手机为：华为P10，型号：VTR-AL00")
    input("请按Enter键确认开始")
elif ss=="2":
    print("华为Mate20；型号：LYA-AL00")
    input("请按Enter键确认开始")
elif ss=="3":
    print("三星Note10，型号：SM-N9700")
    input("请按Enter键确认开始")
#ss=os.popen('adb shell getprop ro.product.model').read()
#list1={"model":ss.strip()}
count1 = 0
count2 = 0
while flag:
    #打开和关闭谷歌确保不会锁屏
    # 3.打开chrome
    #win32api.ShellExecute(0,'open', r'C:\Users\sky.jianghuakun\AppData\Local\Google\Chrome\Application\chrome.exe','','',1)
    #time.sleep(2)
    # 3.关闭chrome
    #os.system("taskkill /F /IM chrome.exe")
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.quit()
    d = u2.connect()
    d.healthcheck()  # 解锁屏幕并启动uiautomator服务


    time.sleep(2)
    if ss=="3":
        try:
            # 使用adb打开设置
            # os.system('adb shell am start com.android.settings/com.android.settings.Settings')
            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            d.xpath('//*[@content-desc="设置"]').click()
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            pass
        try:
            # 使用adb打开设置
            # os.system('adb shell am start com.android.settings/com.android.settings.Settings')
            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            d.xpath(
                '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[2]').click()
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            pass
        try:
            # 使用adb打开设置
            # os.system('adb shell am start com.android.settings/com.android.settings.Settings')
            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            d.xpath('//*[@text="蓝牙"]').click()
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            pass
        toc = time.clock()
        tt = "测试时间: " + "%.2f" % (toc - tic) + " s"
        print(tt)
        try:
            # 使用adb打开设置
            # os.system('adb shell am start com.android.settings/com.android.settings.Settings')
            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            text1=d.xpath('//*[@resource-id="android:id/summary"]').get_text()
            if "已建立用于通话和音频的连接" in text1:
                count1=0
            else:
                count1 += 1
                starttime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
                d.screenshot("%s.jpg" % starttime)
                time.sleep(2)
                d.push("%s.jpg" % starttime, "/sdcard/0pics/")
                if count1 > 10:
                    flag = False
                else:
                    pass
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            count1 += 1
            starttime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            d.screenshot("%s.jpg"%starttime)
            time.sleep(2)
            d.push("%s.jpg"%starttime, "/sdcard/0pics/")
            if count1 > 10:
                flag = False
            else:
                pass

    elif ss=="2":
        print("华为Mate20")
        try:
            # 使用adb打开设置
            # os.system('adb shell am start com.android.settings/com.android.settings.Settings')
            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            d.xpath('//*[@content-desc="设置  1 条通知"]').click()
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            d.xpath('//*[@content-desc="设置"]').click()
            time.sleep(2)
        try:
            d.xpath(
                '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[8]').click()
            time.sleep(1)
        except:
            pass

        try:
            d.xpath('//*[@text="蓝牙"]').click()
        except:
            pass
        toc = time.clock()
        tt = "测试时间: " + "%.2f" % (toc - tic) + " s"
        print(tt)
        try:
            print(d.xpath('//*[@text="已连接用于通话和媒体的音频"]').get_text())
        except:
            d.screenshot("Screenshot.jpg")
            time.sleep(2)
            d.push("Screenshot.jpg", "/sdcard/0pics/")
            flag = False
    elif ss=="1":
        print("华为P10")
        try:
            # 使用adb打开设置

            # d.app_start('com.android.settings.Settings')
            # 华为应用市场
            # d.app_start("com.huawei.appmarket")
            # 打开音乐
            # d.app_start("com.android.mediacenter")

            # 微信
            # d.app_start("com.tencent.mm")
            d.xpath('//*[@text="设置"]').click()
            #os.system('adb shell am start -n  com.android.settings/com.android.settings.HWSettings')
            # 打开相机
            # d.app_start("com.huawei.camera")
            time.sleep(2)
        except:
            pass
        try:
            d.xpath(
                '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[8]').click()
            time.sleep(1)
        except:
            pass

        try:
            d.xpath('//*[@text="蓝牙"]').click()
        except:
            pass
        toc = time.clock()
        tt = "测试时间: " + "%.2f" % (toc - tic) + " s"
        print(tt)
        try:
            text1 =d.xpath('//*[@text="已连接用于通话和媒体的音频"]').get_text()
            if "已连接用于通话和媒体的音频" ==text1:
                count1=0
            else:
                count1 += 1
                starttime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
                d.screenshot("%s.jpg" % starttime)
                time.sleep(2)
                d.push("%s.jpg" % starttime, "/sdcard/0pics/")
                if count1 > 10:
                    flag = False
                else:
                    pass

        except:
            count1 += 1
            starttime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
            d.screenshot("%s.jpg" % starttime)
            time.sleep(2)
            d.push("%s.jpg" % starttime, "/sdcard/0pics/")
            if count1 > 10:
                flag = False
            else:
                pass













