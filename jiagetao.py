#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ps:实现销售管理_价格套（编码搜索、状态选择、修改价格套）

'''
import time
from time import sleep
import unittest
from symbol import except_clause
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
def xiaos(driver):
    time.sleep(1)
    #点击销售管理
    driver.find_element_by_xpath("//*[text()='销售管理']").click() 
    time.sleep(1)
    #点击价格套
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/ul/li[3]/ul/li[3]").click()
    time.sleep(2)
    #获取页面某个元素的属性
    driver.find_element_by_xpath("//*[@class='el-button mb10px el-button--primary']").get_attribute('type')
    a=driver.find_element_by_xpath("//*[@class='el-button mb10px el-button--primary']").get_attribute('type')
    time.sleep(1)
   #判断该属性是否正确
    print ('a=',a)
    if a=='button':
        print('价格套页面元素_断言成功')
        time.sleep(1)
        #点击价格套编码框并输入内容（通过xpath方式定位）
        driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[1]/form/div[1]/div/div/input").send_keys(u"zskx_fs02")
        #点击查询按钮（通过xpath定位）
        #driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div[1]/form/div[5]/div/button[1]/span").click()
        driver.find_element_by_xpath("//*[text()='查询']").click() 
        time.sleep(2)
        #点重置按钮(1)
        #driver.find_element_by_css_selector("input[class='el-button el-button--danger']").click()
        driver.find_element_by_xpath("//*[text()='重置']").click() 
        #点重置按钮(2)
        #driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div[1]/form/div[5]/div/button[2]/span").click()
        time.sleep(1)
        #点击状态选择框
        driver.find_element_by_css_selector("input[placeholder='全部']").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[2]").click()
        #点击查询按钮(用text方式比较好)
        #driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div[1]/form/div[5]/div/button[1]/span").click()
        driver.find_element_by_xpath("//*[text()='查询']").click() 
        time.sleep(2)
        #点击查看'zskx_fs01'
        #driver.find_element_by_xpath("//*[@id='content-wrap']/div/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/div/button").click()
        driver.find_element_by_xpath("//*[text()='zskx_fs01']").click() 
        print('已进入价格套修改页面')
        
        time.sleep(2)
        #在价格套里输入123
        driver.find_element_by_xpath("//*[@id='content-wrap']/div/div[2]/div[2]/form/div[2]/div/div/input").send_keys("123")
        time.sleep(2)
        #模拟点击键盘的翻页按钮
        driver.find_element_by_class_name("el-submenu__title").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_xpath("//*[text()='保存']").click()
        time.sleep(3)
        all=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/p").text
        #print(alert)
        time.sleep(1)
        if all=='保存成功，即将返回列表页':
            print('修改价格套_保存成功')
            
            #点击esc取消键
            #driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/p").send_keys(Keys.ESCAPE)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]/span").click()
            #driver.find_element_by_css_selector("body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--primary > span").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[text()='销售管理']").click()
            time.sleep(2)
            

        else:
            print('修改价格套_保存失败')
        return all
            
        '''
        #判断页面是否有class为el-button.........
        def isElementExist(css):
            try:
                #driver.find_element_by_class_name(css)
                driver.find_element_by_xpath(css)
                return True
            except:
                return False
        
        jieguo=isElementExist("/html/body/div[2]/div/div[2]/div[2]/p")
        
        print ('jieguo=',jieguo)
        if jieguo==True:
            print('页面元素存在--断言成功')
        elif jieguo==False:
            print('没有找到元素页面不存在--断言失败')
            time.sleep(4)
            #点击返回回到价格套页面
            driver.find_element_by_xpath("//*[text()='返回']").click()   
        else:
            print('函数未调用或调用异常')
          
             
  
     #使用函数实现滚动条操作
        def wei():
            if driver.name == "firefox":
                js = "window.scrollTo(0,document.body.scrollHeight)" 
            else:
                js = "window.scrollTo(0,0)" 
            return driver.execute_script(js)          
        wei() 
       
        print('价格套板块执行完毕')   
    else:
        print('价格套_断言失败')
      '''  
        