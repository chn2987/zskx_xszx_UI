#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年10月17日

@author: chen
'''
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
def shous_guanli(driver):
    time.sleep(2)
    #driver.find_element_by_xpath("//*[text()='销售管理']").click()
    time.sleep(1)
    #driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/ul/li[3]/ul/li[1]").click()
    time.sleep(1)
    chen=driver.find_element_by_xpath("//*[text()='添加选品']").text
    #print(chen)
    driver.find_element_by_xpath("//*[text()='添加选品']").click()
    time.sleep(2)
    #driver.find_element_by_class_name("el-dialog__headerbtn").click()#点击取消按钮
    #driver.find_element_by_class_name("el-button el-button--success").click()
    #driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[5]/div/div[2]/div/div[4]/button[3]/span").click()
    driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[5]/div/div[2]/div/div[4]/button[3]/span").click()
    
    time.sleep(2)
    return chen    
    #time.sleep(5)


