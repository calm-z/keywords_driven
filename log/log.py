import logging
import time
import os


class Logger:

    def get_logger(self):
        # 创建一个logger
        logger = logging.getLogger()
        # Log等级总开关
        logger.setLevel(logging.INFO)

        # 设置日志文件的名称
        logfile_time = time.strftime('%Y%m%d', time.localtime(time.time()))
        logfile_path = os.path.dirname(os.getcwd()) + '\\log\\'
        logfile_name = logfile_path + logfile_time + '.txt'

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s-%(filename)s-%(funcName)s-[line%(lineno)d]-%(levelname)s:%(message)s')

        if not logger.handlers:
            # 创建一个日志文件handler对象
            logfile_handler = logging.FileHandler(logfile_name, 'a')
            # 设置输出到file的log等级
            logfile_handler.setLevel(logging.DEBUG)

            # 创建控制台handler对象
            stream_handler = logging.StreamHandler()
            # 设置输出到控制台的log等级
            stream_handler.setLevel(logging.DEBUG)

            logfile_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)

            # 为logger添加handler
            logger.addHandler(logfile_handler)
            logger.addHandler(stream_handler)

        return logger


if __name__ == "__main__":
    Logger().get_logger().debug("这次行么")
    try:
        open('/path/to/does/not/exist', 'rb')
    # except (SystemExit, KeyboardInterrupt):
    #     raise
    except Exception as e:
        Logger().get_logger().error(e, exc_info=False)
        Logger().get_logger().debug(e)
