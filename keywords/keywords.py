# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 12:12
# 工具：PyCharm
# Python版本：3.7

# 导入selenium包
from selenium import webdriver
from selenium.webdriver.common.by import By
from options.options import Options


# 创建关键字类
class Keywords:
    driver = webdriver.Chrome(options=Options().chrome_options())

    # def __init__(self):
    #     self.driver = webdriver.Chrome(options=Options().chrome_options())

    def __init__(self, url, by_type, by_value, text, time):
        self.url = url
        self.by_type = by_type
        self.by_value = by_value
        self.text = text
        self.time = time

    # 隐式等待
    def wait(self, time):
        self.driver.implicitly_wait(self.time)

    # 访问指定URL
    def visit(self, url):
        self.driver.get(self.url)

    # 定位元素
    def locator(self, by_type, by_value):
        return self.driver.find_element(getattr(By(), self.by_type), self.by_value)

    # 清空input框
    def input(self, by_type, by_value):
        return self.locator(self.by_type, self.by_value).clear()

    # 输入
    def clear(self, by_type, by_value, text):
        return self.locator(self.by_type, self.by_value).send_keys(self.text)

    # 点击事件
    def click(self, by_type, by_value):
        return self.locator(self.by_type, self.by_value).click()
