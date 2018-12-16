#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月30日

@author: 现实登录、退出操作..............................
'''
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
#driver = webdriver.Firefox()#调用firefox浏览器
#driver.maximize_window()
#driver.get('http://new.guanli.51dinghuo.cc')
def chen(driver):
    u'''实现登录操作'''
    time.sleep(4)
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("zskxyunying")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("123456")
    time.sleep(1)
    driver.find_element_by_id("loginBtn").click()
    time.sleep(3)

def wei(driver):
    time.sleep(1)
    u'''实现退出操作、并判断页面是否有‘登录’按钮'''
    #driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/span/span").click()
    driver.find_element_by_xpath("//*[text()='超管']").click()
    
    time.sleep(1)
    #driver.find_element_by_xpath("/html/body/ul/li[3]").click()#点击
    driver.find_element_by_xpath("//*[text()='退出']").click()
    try:
       wo=driver.find_element_by_id("loginBtn").text
       return wo
    except:
        print('退出后_在页面中找不到指定元素')
        #return False
  
