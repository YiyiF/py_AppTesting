#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 4:15 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : FiltoHome.py
# @Software: PyCharm


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


class FiltoHome:
    def __init__(self, driver):
        self.driver = driver
        self.homePlusBtn = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'filto other 300 07'
        )))
        self.homeMineTab = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.XPATH, '//XCUIElementTypeStaticText[@name=\"Mine\"]'
        )))

    def clickPlus(self):
        self.homePlusBtn.click()
        albumClose = self.driver.instance.find_element(MobileBy.ACCESSIBILITY_ID, 'filto other 300 04')
        assert albumClose, 'Can\'t open album view.'


    # def clickMine(self):
    #     self.homeMineTab.click()
    #     self.settingBtn = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
    #         MobileBy.XPATH, '//XCUIElementTypeStaticText[@name=\"Mine\"]'

    # def plusdo(self, num1, num2):
    #     self.clicknumber(num1)
    #     self.plus.click()
    #     self.clicknumber(num2)
    #
    #     result = sum((num1, num2))
    #     calcResult = int(self.result.text)
    #
    #     assert result == calcResult, 'Result is different from python.'
    #
    # def multiplydo(self, num1, num2):
    #     self.clicknumber(num1)
    #     self.multiply.click()
    #     self.clicknumber(num2)
    #
    #     result = num1 * num2
    #     calcResult = int(self.result.text)
    #
    #     assert result == calcResult, 'Result is different from python.'
