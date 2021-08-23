#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 8:51 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : FiltoImage.py
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


class FiltoImage:
    def __init__(self, driver):
        self.driver = driver
        self.homePlusBtn = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, '测试素材'
        )))

        el1 = driver.find_element_by_accessibility_id("VIDEOS")
        el1.click()
        el1.click()
        el2 = driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Filto\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[13]/XCUIElementTypeOther[2]")
        el2.click()
        TouchAction(driver).tap(x=128, y=738).perform()
        TouchAction(driver).tap(x=371, y=84).perform()
        el3 = driver.find_element_by_accessibility_id("filto edit 300 82")
        el3.click()
        el4 = driver.find_element_by_accessibility_id("filto public 300 21")
        el4.click()