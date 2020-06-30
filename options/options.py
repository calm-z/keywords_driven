# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 13:40
# 工具：PyCharm
# Python版本：3.7

# 导入selenium包
from selenium import webdriver


# 定义Chrome选项类
class Options:
    # 定义Chrome选项方法

    def chrome_options(self):
        options = webdriver.ChromeOptions()
        # 浏览器窗口最大化
        options.add_argument('start-maximized')
        # 浏览器去除黄条警告
        options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
        # 浏览器去除开发者警告
        options.add_experimental_option('useAutomationExtension', False)

        return options
