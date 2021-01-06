#!/usr/bin/python3
import bluetooth
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.quit()
target_name = "My Device"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print(bdaddr)
    if target_name == bluetooth.lookup_name(bdaddr):
        print(1)
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")


