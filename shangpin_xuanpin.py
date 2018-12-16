#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年10月23日

@author:按照商品名称_搜索商品
'''
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
def xuanpin(driver):
    time.sleep(1)
    driver.find_element_by_xpath("//*[text()='销售管理']").click()
    time.sleep(2)
    #driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/ul/li[3]/ul/li[1]").click()
    driver.find_element_by_xpath("//*[contains(text(),'商品选品')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[1]/form/div[3]/div/div/input").send_keys(u'珍妮诗发水去屑营养260g')
    time.sleep(1)
    driver.find_element_by_xpath("//*[text()='查询']").click()
    #driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div[1]/form/div[11]/div/button[1]/span").click()
    chen=driver.find_element_by_xpath("//*[text()='珍妮诗发水去屑营养260g']").text
    if chen=='珍妮诗发水去屑营养260g':
        print('搜索断言成功')
    else:
        print('搜索断言失败')
    time.sleep(4)
   