#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 8:51 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : webdriver.py
# @Software: PyCharm


from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            "automationName": "XCUITest",
            "platformName": "iOS",
            "udid": "292e1b66e02402ecbd66c1a3321fa55817b7ea21",
            "appName": "Filto",
            "deviceName": "iPhone6s"
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

