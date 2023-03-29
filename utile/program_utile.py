import subprocess
from datetime import time
from pywinauto import Application
from utile.constant_config import MAIN_WINDOW, APP_PATH, APP_DIR
from utile.exception_utile import ControlNotFoundException
from utile.text_utile import set_text


# 连接程序
def start_program(app_path=APP_PATH, app_dir=APP_DIR):
    subprocess.Popen([app_path], cwd=app_dir)


# 连接操作程序的窗口，执行操作
def connect_program(title=MAIN_WINDOW):
    while True:
        try:
            app = Application(backend="uia").connect(title_re=title, timeout=5)
            print(f"链接：{title} 程序成功")
            return app
        except TimeoutError:
            print("连接失败，请检查地址是否配置正确")
            time.sleep(1)


# 操作窗口，先输入文本再进行按钮点击的操作
def operation_window(app, params, win_name=MAIN_WINDOW):
    win = app.window(title_re=win_name)
    print(f"成功获取操作窗口：{win_name}")

    for item in params.get('input', []):
        target_control = win.child_window(title=item[0])
        if target_control.exists():
            set_text(target_control, item[1])
        else:
            print(f"未找到目标控件，参数为：{item[0]}")
            raise ControlNotFoundException("未找到控件")

    for item in params.get('click', []):
        target_control = win.child_window(title=item)
        if target_control.exists():
            target_control.click_input()
            # target_control.invoke()
        else:
            print(f"未找到目标控件，参数为：{item}")
            raise ControlNotFoundException("未找到控件")

# 双击然后输入文本内容
