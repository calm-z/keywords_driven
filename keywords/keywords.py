# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 12:12
# 工具：PyCharm
# Python版本：3.7


# 导入selenium包
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from options.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from log.log import Logger
import win32gui
import win32con


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
        param['by_type'] = value[2]  定位方法
        param['by_value'] = value[3] 元素路径
        param['text'] = value[4]     输入内容
        param['expect'] = value[6]   预期结果
    """

    log = Logger().get_logger()

    # 构造函数 实例化浏览器驱动,调用open_browser
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

    # 定位元素,并返回该元素
    def locator(self, **kwargs):
        try:
            return self.driver.find_element((getattr(By, kwargs['by_type'].upper())), kwargs['by_value'])
        except Exception as e:
            print('元素定位失败，信息：{0}'.format(e))

    # 调用locator后，对元素进行清空操作
    def clear(self, **kwargs):
        self.locator(**kwargs).clear()

    # 调用locator后，对元素进行输入操作
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['text'])

    # 调用locator后，对元素进行点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 为实例化的浏览器驱动设置隐式等待，传入时间
    def wait(self, **kwargs):
        self.driver.implicitly_wait(kwargs['text'])

    # 使用time模块下的sleep实现强制等待
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

    # 为元素设置焦点
    def focus(self, **kwargs):
        self.driver.execute_script("arguments[0].focus();", self.locator(**kwargs))

    # 为元素取消焦点
    def blur(self, **kwargs):
        self.driver.execute_script("arguments[0].blur();", self.locator(**kwargs))

    # 非input输入框上传文件，需要传入上传的文件地址、浏览器类型
    def upload_not_input(self, **kwargs):
        """
            通过pywin32模块实现文件上传的操作
            ：param file_path 文件的绝对路径
            ：param browser_type 浏览器类型
            ：return
        """
        browser_type = kwargs['text']
        file_path = kwargs['by_value']
        try:
            if browser_type.lower() == 'chrome':
                title = "打开"
            elif browser_type.lower() == 'firefox':
                title = "文件上传"
            elif browser_type.lower() == 'ie':
                title = "选择要加载的文件"
            else:
                self.log.info("未定义的浏览器类型->{0}，非input输入框上传文件失败，请更改浏览器！".format(browser_type))

            # 找元素
            # 一级窗口“#32770”,"打开"
            dialog = win32gui.FindWindow("#32770", title)
            # 向下传递
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
            # 编辑按钮
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            # 打开按钮
            button = win32gui.FindWindowEx(dialog, 0, 'Button1', "打开(&O)")  # 二级
            # 输入文件的绝对路径，点击“打开”按钮
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)  # 发送文件路径
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        except Exception as e:
            self.log.info("非input输入框上传文件失败，错误信息{0}".format(e))

    # 切换alert
    def switch_to_alert(self, **kwargs):
        alt = self.driver.switch_to.alert
        self.log.info("alert框文本内容：{0}".format(alt.text))
        option = kwargs['by_type']
        try:
            if option == 'accept':
                alt.accept()
            elif option == 'dismiss':
                alt.dismiss()
            elif option == 'prompt':
                alt.send_keys(kwargs['text'])
                alt.accept()
        except Exception as e:
            self.log.error("alert操作失败，错误信息：{0}".format(e))

    # 定位元素，并模糊匹配该元素的文本内容
    def assert_fazzy(self, **kwargs):
        try:
            text = self.locator(**kwargs).text

            if kwargs['expect'] in text:
                self.log.info('元素文本匹配成功')
                return True
            else:
                self.log.info('{0} != {1},匹配失败'.format(text, kwargs['expect']))
                return False
        except Exception as e:
            self.log.error('匹配元素文本失败，信息：{0}'.format(e))

    # 鼠标悬停
    def mouse_hover(self, **kwargs):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.locator(**kwargs)).perform()
            self.log.info("鼠标悬停成功")

        except Exception as e:
            self.log.error('mouse_hover操作失败，错误信息：{0}'.format(e))

    # 查找元素，获取属性值并断言文本是否存在在属性值中
    def assert_attribute(self, **kwargs):
        el = self.locator(**kwargs)
        try:
            attribute = el.get_attribute(kwargs['text'])
            if kwargs['expect'] in attribute:
                self.log.info('属性值{0}在元素中'.format(kwargs['expect']))
                return True
            else:
                self.log.info('属性{0}没有在该元素中'.format(kwargs['expect']))
                return False

        except Exception as e:
            self.log.error('获取属性值断言失败，错误信息：{0}'.format(e))

    # 操作页面滚动，需要传入滚动参数
    def scrolling(self, **kwargs):
        try:
            js = "window.scrollTo" + kwargs['text']
            print(js)
            self.driver.execute_script(js)
            self.log.info('页面滚动{0}成功'.format(kwargs['text']))
        except Exception as e:
            self.log.error('页面滚动失败，错误信息：{0}'.format(e))

    # 获取当前页面的url并断言
    def assert_url(self, **kwargs):
        try:
            url = self.driver.current_url
            assert url == kwargs['expect']
            self.log.info('断言url成功:{0}'.format(url))
            return True
        except Exception as e:
            self.log.error('断言当前页面的url失败,{0} != {1}'.format(url, kwargs['expect']))
            return False


if __name__ == "__main__":
    param1 = {'by_type': '', 'by_value': '"]', 'text': 'https://baidu.com', 'expect': ''}
    param2 = {'by_type': 'xpath', 'by_value': '//*[@id="s-hotsearch-wrapper"]/div/a[1]/div', 'text': '5',
              'expect': '百度热榜'}

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
