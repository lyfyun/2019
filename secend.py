#!C:\Users\nb07.it.staff01\AppData\Local\Programs\Python
# -*- coding:utf-8 -*-
# @Time    : 2019/8/19 10:02
# @Author  : liyong
# @File    : secend.py
# @Version : v1.0
#实现页面点击切换选项卡
#实现自动截图并保存至指定文件夹内

import time,datetime,pymysql
import os
from selenium import webdriver
from time import sleep
from PIL import ImageGrab
from pymouse import *

#创建截图文件夹
daytime1 = datetime.datetime.now().strftime('%Y%m%d0800')
daytime2 = datetime.datetime.now().strftime('%Y%m%d1200')
daytime3 = datetime.datetime.now().strftime('%Y%m%d1600')
daytime4 = datetime.datetime.now().strftime('%Y%m%d2000')

pwd1 = "//137.83.50.109//it//每日工作截图//防火墙(备)//"+daytime1
pwd2 = "//137.83.50.109//it//每日工作截图//防火墙(备)//"+daytime2
pwd3 = "//137.83.50.109//it//每日工作截图//防火墙(备)//"+daytime3
pwd4 = "//137.83.50.109//it//每日工作截图//防火墙(备)//"+daytime4

word_name1 = os.path.exists(pwd1)
word_name2 = os.path.exists(pwd2)
word_name3 = os.path.exists(pwd3)
word_name4 = os.path.exists(pwd4)

url = 'https://10.49.160.5:8443/login.html?lang=zh_CN'
chromedriver = "E:\chromedriver.exe"''
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)   # 声明浏览器对象

driver.get(url)    #访r问页面
driver.maximize_window()
m = PyMouse()
m.click(1577,93)

#输入账号密码
driver.find_elements_by_xpath('//*[@id="loginForm-body"]')[0].click()
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("edp")
driver.find_element_by_id('platcontent').send_keys("Edp@123456")
driver.find_element_by_id('login_middle').click()

sleep(10)

if not word_name1:
    os.makedirs(pwd1)
    
    bbox = ()#第一份截图
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'_m1.jpg')
    driver.find_element_by_id('topmenu_network').click()
    sleep(5)
    #第二份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'_m2.jpg')
    driver.find_elements_by_xpath('//*[@id="gre-cfg"]')[0].click()
    driver.find_element_by_id('grepanel-cfg-tree-leaf').click()
    sleep(5)
    #第三份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'_m3.jpg')
elif not word_name2:
    os.makedirs(pwd2)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'_m1.jpg')
    driver.find_element_by_id('topmenu_network').click()
    sleep(5)
     #第二份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'_m2.jpg')
    driver.find_elements_by_xpath('//*[@id="gre-cfg"]')[0].click()
    driver.find_element_by_id('grepanel-cfg-tree-leaf').click()
    sleep(5)
    #第三份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'_m3.jpg')
elif not word_name3:
    os.makedirs(pwd3)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'_m1.jpg')
    driver.find_element_by_id('topmenu_network').click()
    sleep(5)
     #第二份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'_m2.jpg')
    driver.find_elements_by_xpath('//*[@id="gre-cfg"]')[0].click()
    driver.find_element_by_id('grepanel-cfg-tree-leaf').click()
    sleep(5)
    #第三份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'_m3.jpg')
elif not word_name4:
    os.makedirs(pwd4)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'_m1.jpg')
    driver.find_element_by_id('topmenu_network').click()
    sleep(5)
     #第二份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'_m2.jpg')
    driver.find_elements_by_xpath('//*[@id="gre-cfg"]')[0].click()
    driver.find_element_by_id('grepanel-cfg-tree-leaf').click()
    sleep(5)
    #第三份截图
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'_m3.jpg')

driver.quit()

#os.system('taskkill /im chromedriver.exe /F')
