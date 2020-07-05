"""
_*_ coding = utf-8 _*_ 
Author:calm-zn
@time:2020/7/5
"""

from excel.excel_conf import Excel_conf
from keywords.keywords import Keywords
from log.log import Logger


class Excel_excutor(object):
    '''
        实例化对象
        结合参数调用关键字
        封装整合
    '''
    # 创建日志对象
    log = Logger().get_logger()

    # excel执行读写操作
    def excute_web(self, yaml_path, key1, key2):
        ec = Excel_conf()
        file_data = ec.load_yaml(yaml_path)
        excel_path = file_data[key1][key2]
        excel = ec.open_excel(excel_path)
        sheets = ec.get_sheets(excel)

        try:
            # 读取所有的sheet表
            for sheet in sheets:
                self.log.info('获取{0}内容成功，现在开始执行自动化测试......'.format(sheet))
                sheet_now = excel[sheet]
                # 基于sheet内容，运行测试用例
                for value in sheet_now.values:
                    param = {}
                    param['by_type'] = value[2]
                    param['by_value'] = value[3]
                    param['text'] = value[4]
                    param['expect'] = value[6]

                    # 判断文件，从用例内容开始执行
                    if type(value[0]) is int:

                        # 判断关键字，如果是open_browser，则实例化对象，若不是，则进行其他元素操作
                        if value[1] == 'open_browser':
                            self.log.info('现在执行关键字：{0}，操作描述{1}'.format(value[1], value[5]))
                            wk = Keywords(param['text'])
                            self.log.info("打开浏览器啊")

                        # 判断是否为断言，若是断言则添加写入操作
                        elif 'assert' in value[1]:
                            self.log.info('现在执行关键字：{0}，操作描述：{1}'.format(value[1], value[5]))
                            status = getattr(wk, value[1])(**param)
                            row = value[0] + 1
                            if status is True:
                                self.log.info('流程测试通过！')
                                ec.cell_write('pass', sheet_now, row)
                            else:
                                self.log.info('流程测试失败！')
                                ec.cell_write('false', sheet_now, row)
                            ec.excel_save(excel, excel_path)
                        # 定义常规关键字调用
                        else:
                            self.log.info('现在执行关键字：{0}，操作描述：{1}'.format(value[1], value[5]))
                            getattr(wk, value[1])(**param)

                    else:
                        pass

        except Exception as e:
            self.log.exception('运行出现异常，信息描述{0}：'.format(e))
        finally:
            # 关闭读取的文件
            self.log.info("文件读取完毕，自动化执行结束！\n")
            ec.close(excel)


if __name__ == '__main__':
    yaml_path = r'../config/data.yml'
    key1 = 'webui'
    key2 = 'file'
    Excel_excutor().excute_web(yaml_path, key1, key2)
