# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 14:40
# 工具：PyCharm
# Python版本：3.7

from keywords.keywords import Keywords
from time import sleep
from log.log import Logger

Keywords().wait(10)
Keywords().visit("https://baidu.com")
sleep(5)

Keywords().input('ID', 'kw', '关键字驱动测试')
Keywords().click('id', 'su')

# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')
#
# driver = webdriver.Chrome(options=options)
# driver.get('https://baidu.com')
# driver.find_element_by_id('kw').send_keys()
