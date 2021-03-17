# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2021/3/15 17:32
# 工具：PyCharm
# Python版本：3.7
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from options.options import Options
from keywords.keywords import Keywords

driver = webdriver.Chrome(options=Options().chrome_options())
driver.implicitly_wait(10)
driver.get("https://www.100.nxdev.cn/")
course_list = driver.find_element_by_xpath("//a[@class='item router-link-exact-active active']")

# 通过selenium获取元素属性
el = driver.find_element_by_xpath('//a[@href="/pc/course-list"]')
value = el.get_attribute('class')
if 'active' in value:
    print("这个元素状态是被选中的哦")
time.sleep(2)
js = "window.scrollTo(0,20000)"

driver.execute_script(js)

# # 通过Document对象来修改元素属性
# js = "document.getElementById('ai-topsearch').setAttribute('value','asd')"
# # 执行js语句函数：js执行器
# driver.execute_script(js)
#
# # 如何有效地运行js语句
# el = driver.find_element_by_xpath()
# js = "arguments[0].innerHTML='虚竹'"
# # 灵活版js执行器操作：通过传递元素参数，来快速实现元素的识别与操作
# driver.execute_script(js,el)

driver.find_element_by_xpath('//a[@href="/pc/my-course"]').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/button').click()
driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').send_keys('17615270450')
driver.find_element_by_xpath('//input[@placeholder="请输入短信验证码"]').send_keys('1111')
driver.find_element_by_xpath('//button[@class="el-button button el-button--primary is-round"]').click()
time.sleep(2)
driver.find_element(By.Link_text,'')
