#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年10月8日

@author: chen
'''
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Firefox()#调用firefox浏览器
driver.maximize_window()
driver.get('http://new.guanli.51dinghuo.cc')
time.sleep(4)
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("zskxyunying")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")
time.sleep(1)
driver.find_element_by_id("loginBtn").click()
time.sleep(3)
driver.find_element_by_xpath("//*[text()='基础设置']").click()
driver.find_element_by_class_name("el-menu-item").click()
ww=driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div[2]/div[1]/button[1]/span").text
print (ww)



time.sleep(3)

