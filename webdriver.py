#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 8:51 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : webdriver.py
# @Software: PyCharm


from appium import webdriver
import os


def get_usbconnect_device():
    cmd = "tidevice list"
    result = os.popen(cmd).readlines()
    udid, name = result[0].strip().split(' ', 1)
    return udid, name


device_udid, device_name = get_usbconnect_device()


class Driver:
    def __init__(self):
        desired_cap = {
            "automationName": "XCUITest",
            "platformName": "iOS",
            "udid": device_udid,
            "appName": "Filto",
            "bundleId": "com.pinsotech.filto",
            "deviceName": device_name
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
