#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年10月23日

@author: 实现供货商资料管理，搜索供货商
'''
import time
from time import sleep
from selenium import webdriver
import unittest
#打开供货商并获取'新增供货商按钮的值'
def dede(driver):
    time.sleep(2)
    u'''进入基础设置页面'''
    driver.find_element_by_xpath("//*[text()='基础设置']").click()
    driver.find_element_by_class_name("el-menu-item").click()
    ww=driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[2]/div[1]/button[1]/span").text
    return ww
    time.sleep(2)
#搜索供货商名称，并返回一个结果
def soso(driver):
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[1]/form/div[2]/div/div/input").send_keys(u"速度大大")
    #driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[1]/form/div[8]/div/button[1]/span").click()
    driver.find_element_by_xpath("//*[text()='搜索']").click()
    time.sleep(2)
    #chen=driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[3]/div[3]/table/tbody/tr/td[4]/div").text
    chen=driver.find_element_by_xpath("//*[text()='速度大大']").text
    return chen
    
    
