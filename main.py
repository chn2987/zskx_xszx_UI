#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月30日
@author: 主函数、主要实现模块调用及断言处理
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
import unittest
import login
import xiaoshou_guanli
import gonghuoshang
import jiagetao
import shangpin_xuanpin
#定义一个类并继承unittest模块TestCase
class BolgHome(unittest.TestCase):
    u'''销售中心自动化'''
    @classmethod
    def setUpClass(self):#开始操作的函数
        self.driver = webdriver.Firefox()
        url = "http://new.guanli.51dinghuo.cc"
        self.driver.get(url)
        self.driver.maximize_window()#浏览器最大化
        #self.driver.implicitly_wait(30)
    @classmethod
    def tearDownClass(self):
        #结束浏览器操作
        self.driver.quit()
    def test_01(self):#登录操作
        u'''判断是否登录成功：'''
        login.chen(self.driver)#调用login模块chen方法
        Title=self.driver.title
        Title1='销售中心 - 掌上快销'
        self.assertEqual(Title, Title1, 'title不一致登录失败')
    def test_07(self): #退出操作
        u'''退出系统验证：'''
        fanhui=login.wei(self.driver)#调用login模块wei方法
        self.assertEqual(fanhui, '登录', '未找到登录_退出系统失败')#断言
    def test_02(self):#进入供货商资料
        u'''验证供货商_是否有新增按钮'''
        fanhui2=gonghuoshang.dede(self.driver)
        self.assertEqual(fanhui2, '新增供货商', '验证供货商资料中_有没有新增供货商按钮——验证失败')
    def test_03(self):#搜索供货商名称
        u'''供货商名称搜索'''
        sousuo=gonghuoshang.soso(self.driver)
        self.assertEqual(sousuo, '速度大大', '供货商资料中_没有搜索到 速度大大')       
    def test_04(self):#调用价格套模块
        u'''价格套操作流程断言'''
        tao=jiagetao.xiaos(self.driver)
        self.assertEqual(tao, '保存成功，即将返回列表页', '修改价格套_保存失败')
         
    def test_05(self):
        u'''商品选品_搜索'''
        pin=shangpin_xuanpin.xuanpin(self.driver)
  
    def test_06(self):#商品选品
        u'''商品选品_上传'''
        xiao=xiaoshou_guanli.shous_guanli(self.driver)
        self.assertEqual(xiao, '添加选品', '实际结果没有商品选品_断言失败')  
        
if __name__ == "__main__":
    unittest.main()