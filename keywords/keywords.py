# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 12:12
# 工具：PyCharm
# Python版本：3.7

# 导入selenium包
from selenium import webdriver
from selenium.webdriver.common.by import By
from options.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


# 创建浏览器对象，通过反射机制来实现
def open_browser(browser_type):
    # 添加异常处理机制，确保健壮性
    # noinspection PyBroadException
    try:
        if browser_type == 'Chrome':
            driver = webdriver.Chrome(options=Options().chrome_options())
        else:
            driver = getattr(webdriver, browser_type)()
    except Exception as e:
        driver = webdriver.Chrome()
    return driver


class Keywords:

    # 构造函数
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 访问指定URL
    def visit(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, by_type, by_value):
        return self.driver.find_element(getattr(By, by_type.upper()), by_value)

    # 清空操作
    def clear(self, by_type, by_value):
        self.locator(by_type, by_value).clear()

    # 输入操作
    def input(self, by_type, by_value, text):
        self.locator(by_type, by_value).send_keys(text)

    # 点击操作
    def click(self, by_type, by_value):
        self.locator(by_type, by_value).click()

    # 隐式等待
    def wait(self, time):
        self.driver.implicitly_wait(time)

    # 强制等待
    def sleep(self, time):
        sleep(time)

    # 显式等待
    def explicit_wait(self, by_type, by_value, text, time):
        wait = WebDriverWait(self.driver, text, time)
        return wait.until(lambda el: self.locator(by_type, by_value), message="元素定位失败")

    # 断言
    def assert_txet(self, by_type, by_value, text, time, expect):
        exp = self.explicit_wait(by_type, by_value, text, time)
        reality = exp.text
        try:
            assert reality == expect
            return True
        except Exception as e:
            return False

    # 关闭浏览器当前标签页
    def close(self):
        self.driver.close()

    # 关闭浏览器
    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    wk = Keywords('Chrome')
    wk.wait('10')
    wk.visit('https://baidu.com')
    wk.input('id', 'kw', 'selenium')
    wk.click('id', 'su')
    wk.sleep(1)
    wk.assert_txet()
