from pywinauto import Application, keyboard
from pywinauto import timings
from utile.constant_config import MAIN_WINDOW
from utile.program_utile import connect_program

# 启动或连接到应用程序
app = connect_program()

# # 找到包含表格的窗口
main_window = app.window(title=MAIN_WINDOW)
target_control = main_window.child_window(control_type="Button", title="保存")
# 输入文本
target_control.click_input()
