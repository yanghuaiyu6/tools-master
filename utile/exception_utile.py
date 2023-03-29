# 自定义异常
class ControlNotFoundException(Exception):
    def __init__(self, message="控件未找到"):
        super().__init__(message)
