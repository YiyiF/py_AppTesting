#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:05 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : beforeHome.py
# @Software: PyCharm
from datetime import time

from webdriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

"""
Expected conditions >> Indicate the value for the expected condition.
    EC.visibility_of_element_located，Need to find the element and it is visible.
    EC.presence_of_element_located，Find the element whatever it is visible.
WebDriverWait >> Waiting for some specific element to be reachable and may also receive a timeout value.
MobileBy >> Indicate in a mobile context that can use specific content to find elements.
    find_element_by_ios_uiautomation
    find_elements_by_ios_uiautomation
    find_element_by_android_uiautomator
    find_elements_by_android_uiautomator
    find_element_by_accessibility_id
    find_elements_by_accessibility_id
"""


class FiltoSplash:
    def __init__(self, driver):
        self.driver = driver
        self.splashNextBtn= WebDriverWait(self.driver.instance, 5).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'NEXT'
        )))
        self.subClose = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, ''
        )))
        self.subYearly = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, ''
        )))
        self.subQuarterly = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, ''
        )))
        self.subMonthly = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, ''
        )))
        self.subBtnSub = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, ''
        )))
        self.subBtnRestore = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, ''
        )))

    def set_func(func):
        global num
        num = [0]  # 闭包中外函数中的变量指向的引用不可变

        def call_func():
            func()
            num[0] += 1
            # print("执行次数", num[0])

        return call_func

    @set_func
    def clickNext(self, btn):
        self.splashNextBtn.click()
        if num == 1:
            time.sleep(1)
            splashNextBtnAnother = WebDriverWait(self.driver.instance, 5).until(EC.presence_of_element_located((
                MobileBy.ACCESSIBILITY_ID, 'NEXT'
            )))
            assert splashNextBtnAnother, 'Can\'t find next button in the 2nd Splash video.'

        elif num == 2:
            time.sleep(1)
            splashSubBtn = WebDriverWait(self.driver.instance, 5).until(EC.presence_of_element_located((
                MobileBy.ACCESSIBILITY_ID, 'SUBSCRIBE'
            )))
            assert splashSubBtn, 'Can\'t find subscribe button in the Splash subscription page.'








    def clicknumber(self, num):
        _num = str(num)
        self.driver.instance.find_element(MobileBy.ID, 'com.android.calculator2:id/digit_' + _num).click()
        assert _num in self.number.text, 'Result is different from input.'

    def plusdo(self, num1, num2):
        self.clicknumber(num1)
        self.plus.click()
        self.clicknumber(num2)

        result = sum((num1, num2))
        calcResult = int(self.result.text)

        assert result == calcResult, 'Result is different from python.'

    def multiplydo(self, num1, num2):
        self.clicknumber(num1)
        self.multiply.click()
        self.clicknumber(num2)

        result = num1 * num2
        calcResult = int(self.result.text)

        assert result == calcResult, 'Result is different from python.'

