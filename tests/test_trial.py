#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 4:27 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : test_trial.py
# @Software: PyCharm


import unittest
from pageobjects.FiltoHome import FiltoHome
from webdriver import Driver


class FiltoHomeTests(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_plus(self):
        filtoHome = FiltoHome(self.driver)
        filtoHome.clickPlus()

    def tearDown(self):
        self.driver.instance.quit()
