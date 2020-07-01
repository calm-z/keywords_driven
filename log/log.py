import logging
import time
import os


def log_conf():
    # 设置日志文件的名称
    logfile_time = time.strftime('%Y%m%d', time.localtime(time.time()))
    logfile_path = os.path.dirname(os.getcwd()) + '-Logs-'
    logfile_name = logfile_path + logfile_time + '.log'
    # 创建一个日志文件handler对象
    logfile_handler = logging.FileHandler(logfile_name, 'a')
    # 设置输出到file的log等级
    logfile_handler.setLevel(logging.DEBUG)

    # 创建控制台handler对象
    stream_handler = logging.StreamHandler()
    # 设置输出到控制台的log等级
    stream_handler.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    formatter = logging.Formatter(
        '%(asctime)s-%(filename)s-%(funcName)s-[line%(lineno)d]-%(levelname)s:%(message)s')
    logfile_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)


class Log:
    # 创建一个logger
    logger = logging.getLogger()
    # Log等级总开关
    logger.setLevel(logging.NOTSET)

    def __init__(self):
        # 为logger添加handler
        self.logger.addHandler(log_conf().logfile_handler)
        self.logger.addHandler(log_conf().stream_handler)


if __name__ == "__main__":
    logging.debug("这是怎么了")
    open('/path/to/does/not/exist', 'rb')
    try:
        open('/path/to/does/not/exist', 'rb')
    # except (SystemExit, KeyboardInterrupt):
    #     raise
    except Exception as e:
        Log.logger.debug("这是怎么了")
        Log.logger.error(e, exc_info=False)
        # logger.debug(e)
