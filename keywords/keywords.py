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
from log.log import Logger


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
    """
        param = {}
        param['by_type'] = value[2]
        param['by_value'] = value[3]
        param['text'] = value[4]
        param['expect'] = value[6]
    """
    log = Logger().get_logger()

    # 构造函数
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 访问指定URL
    def visit(self, **kwargs):
        self.driver.get(kwargs['text'])

    # 关闭浏览器当前标签页
    def close(self, **kwargs):
        self.driver.close()

    # 关闭浏览器
    def quit(self, **kwargs):
        self.driver.quit()

    # 定位元素
    def locator(self, **kwargs):
        try:
            return self.driver.find_element((getattr(By, kwargs['by_type'].upper())), kwargs['by_value'])
        except Exception as e:
            print('元素定位失败，信息：{0}'.format(e))

    # 清空操作
    def clear(self, **kwargs):
        self.locator(**kwargs).clear()

    # 输入操作
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['text'])

    # 点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 隐式等待
    def wait(self, **kwargs):
        self.driver.implicitly_wait(kwargs['text'])

    # 强制等待
    def sleep(self, **kwargs):
        sleep(kwargs['text'])

    # 显式等待
    def explicit_wait(self, **kwargs):
        try:
            wait = WebDriverWait(self.driver, kwargs['text'])
            return wait.until(lambda el: self.locator(**kwargs))
        except Exception as e:
            print('显示等待失败，信息：{0}'.format(e))

    # 文本断言
    def assert_text(self, **kwargs):
        reality = self.explicit_wait(**kwargs).text
        try:
            assert reality == kwargs['expect']
            return True
        except Exception as e:
            self.log.info('断言失败，失败信息：{0}!={1}'.format(reality, kwargs['expect']))
            return False


if __name__ == "__main__":
    param1 = {'by_type':'','by_value':'"]','text':'https://baidu.com','expect':''}
    param2 = {'by_type':'xpath','by_value':'//*[@id="s-hotsearch-wrapper"]/div/a[1]/div','text':'5','expect':'百度热榜'}

    wk = Keywords('Chrome')
    # wk.wait()
    wk.visit(**param1)
    # wk.input('id', 'kw', 'selenium')
    # wk.click('id', 'su')
    # wk.sleep(1)
    wk.assert_text(**param2)
    # wk.wait(2)
    wk.close()
    wk.quit()
