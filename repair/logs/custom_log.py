import logging


# 1.设置日志格式、级别和输出文件
def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = logging.INFO
    log_file = "repair/logs/test.log"

    logging.basicConfig(filename=log_file, level=log_level, format=log_format)
