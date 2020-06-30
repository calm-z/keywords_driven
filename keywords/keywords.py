# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 12:12
# 工具：PyCharm
# Python版本：3.7

# 导入selenium包
from selenium import webdriver
from options.options import Options


# 创建关键字类
class Keywords:
    driver = webdriver.Chrome(options=Options().chrome_options())

    # def __init__(self):
    #     self.driver = webdriver.Chrome(options=Options().chrome_options())

    # 隐式等待
    def wait(self, time):
        self.driver.implicitly_wait(time)

    # 访问指定URL
    def visit(self, URL):
        self.driver.get(URL)
