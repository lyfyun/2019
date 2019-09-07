#!C:\Users\nb07.it.staff01\AppData\Local\Programs\Python
# -*- coding:utf-8 -*-
# @Time    : 2019/8/19 10:02
# @Author  : liyong
# @File    : ping.py
# @Version : v1.0
#实现页面点击切换选项卡
#实现自动截图并保存至指定文件夹内

import time,datetime,pymysql
import os
from selenium import webdriver
from time import sleep
from PIL import ImageGrab

#创建截图文件夹
daytime1 = datetime.datetime.now().strftime('%Y%m%d0800')
daytime2 = datetime.datetime.now().strftime('%Y%m%d1200')
daytime3 = datetime.datetime.now().strftime('%Y%m%d1600')
daytime4 = datetime.datetime.now().strftime('%Y%m%d2000')

pwd1 = "//137.83.50.109//it//每日工作截图//RT服务器//"+daytime1
pwd2 = "//137.83.50.109//it//每日工作截图//RT服务器//"+daytime2
pwd3 = "//137.83.50.109//it//每日工作截图//RT服务器//"+daytime3
pwd4 = "//137.83.50.109//it//每日工作截图//RT服务器//"+daytime4

word_name1 = os.path.exists(pwd1)
word_name2 = os.path.exists(pwd2)
word_name3 = os.path.exists(pwd3)
word_name4 = os.path.exists(pwd4)

rt_ip = '10.49.164.1'
au_ip = '137.83.64.18'
idc_ip = '10.201.128.1'

if not word_name1:
    os.makedirs(pwd1)

    os.system('ping -n 20 %s'%rt_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'rt_ip.jpg')

    os.system('ping -n 20 %s'%au_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'au_ip.jpg')

    os.system('ping -n 20 %s'%idc_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd1+'\\'+daytime1+'idc_ip.jpg')
    
elif not word_name2:
    os.makedirs(pwd2)

    os.system('ping -n 20 %s'%rt_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'rt_ip.jpg')
    
    os.system('ping -n 20 %s'%au_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'au_ip.jpg')
    
    os.system('ping -n 20 %s'%idc_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd2+'\\'+daytime2+'idc_ip.jpg')
 
elif not word_name3:
    os.makedirs(pwd3)
    
    os.system('ping -n 20 %s'%rt_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'rt_ip.jpg')

    os.system('ping -n 20 %s'%au_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'au_ip.jpg')

    os.system('ping -n 20 %s'%idc_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd3+'\\'+daytime3+'idc_ip.jpg')

elif not word_name4:
    os.makedirs(pwd4)
        
    os.system('ping -n 20 %s'%rt_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'rt_ip.jpg')

    os.system('ping -n 20 %s'%au_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'au_ip.jpg')

    os.system('ping -n 20 %s'%idc_ip)

    bbox = ()
    im = ImageGrab.grab(bbox)
    im.save(pwd4+'\\'+daytime4+'idc_ip.jpg')


