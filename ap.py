#!C:\Users\nb07.it.staff01\AppData\Local\Programs\Python
# -*- coding:utf-8 -*-
# @Time    : 2019/8/19 10:02
# @Author  : liyong
# @File    : ap.py
#如果系统改变了，需要配置环境变量，关闭IE保护模式
import os
from selenium import webdriver
from pykeyboard import *
from pymouse import *
from time import sleep
import time,datetime,pymysql
from PIL import ImageGrab

m = PyMouse()
k = PyKeyboard()

url = 'http://137.83.253.2/MainApp.html'
IEDriverServer = "C:\Program Files\Internet Explorer\IEDriverServer.exe"''
os.environ["webdriver.IE.driver"] = IEDriverServer
driver = webdriver.Ie(IEDriverServer)   # 声明浏览器对象

driver.get(url)

#窗口最大化
driver.maximize_window()

sleep(3)
m.click(747,431)
k.type_string('visitor')
sleep(1)
m.move(755,480)
m.click(755,480)
k.type_string('auchanvisitor')
sleep(1)
k.tap_key(k.enter_key)
sleep(5)

#创建截图文件夹
daytime1 = datetime.datetime.now().strftime('%Y%m%d0800')
daytime2 = datetime.datetime.now().strftime('%Y%m%d1200')
daytime3 = datetime.datetime.now().strftime('%Y%m%d1600')
daytime4 = datetime.datetime.now().strftime('%Y%m%d2000')

pwd1 = "//137.83.50.109//it//每日工作截图//AP//"+daytime1
pwd2 = "//137.83.50.109//it//每日工作截图//AP//"+daytime2
pwd3 = "//137.83.50.109//it//每日工作截图//AP//"+daytime3
pwd4 = "//137.83.50.109//it//每日工作截图//AP//"+daytime4

word_name1 = os.path.exists(pwd1)
word_name2 = os.path.exists(pwd2)
word_name3 = os.path.exists(pwd3)
word_name4 = os.path.exists(pwd4)

if not word_name1:
    os.makedirs(pwd1)
    
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'_ap.jpg')

elif not word_name2:
    os.makedirs(pwd2)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'_ap.jpg')

elif not word_name3:
    os.makedirs(pwd3)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'_ap.jpg')

elif not word_name4:
    os.makedirs(pwd4)
    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'_ap.jpg')


driver.quit()

#os.system('taskkill /im IEDriverServer.exe /F')
