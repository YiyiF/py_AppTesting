#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 4:47 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : Install.py
# @Software: PyCharm


from tidevice._usbmux import Usbmux
from tidevice import Device
from multiprocessing import Pool
import os


def connect_device():
    devices_list = Usbmux().device_list()
    devices_udid = [item['UDID'] for item in devices_list]
    return devices_udid


def install_app(device_udid, file_or_url):
    print('Run task %s (%s)...' % (device_udid, os.getpid()))
    print('Begin installing APP on device %s ' % device_udid)
    device = Device(device_udid)
    device.app_install(file_or_url)


if __name__ == '__main__':
    file_or_url = ''  # ipa package
    devices_udid = connect_device()

    print('Parent process %s.' % os.getpid())
    pool = Pool(processes=4)
    for i in range(len(devices_udid)):
        pool.apply_async(install_app, args=(devices_udid[i], file_or_url, ))
    pool.close()
    pool.join()

    print('All subprocesses done.')
