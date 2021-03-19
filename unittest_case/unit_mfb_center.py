# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2021/3/19 17:22
# 工具：PyCharm
# Python版本：3.7

import unittest

from excel.excel_excutor import Excel_excutor
from log.log import Logger


class MFB_Center(unittest.TestCase):
    """
    MFB_Center类用于满分班购课中心（web端）测试用例的管理
    """
    log = Logger().get_logger().info('开始执行测试用例')
    yaml_path = '../config/data.yml'
    key1 = 'webui'
    key2 = 'mfb_file'

    def test_visit(self):
        """
        访问购课中心url
        """
        return self
