import logging


# 1.������־��ʽ�����������ļ�
def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = logging.INFO
    log_file = "repair/logs/test.log"

    logging.basicConfig(filename=log_file, level=log_level, format=log_format)
