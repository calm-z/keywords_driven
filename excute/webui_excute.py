# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2020/6/29 14:40
# 工具：PyCharm
# Python版本：3.7

from keywords.keywords import Keywords
from log.log import Logger
from excel.excel_excutor import Excel_excutor

if __name__ == '__main__':
    log = Logger().get_logger().info('开始执行测试用例')
    yaml_path = '../config/data.yml'
    key1 = 'webui'
    key2 = 'mfb_file'
    Excel_excutor().excute_web(yaml_path, key1, key2)
