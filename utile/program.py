import subprocess
import time
from pywinauto import Application

from utile.exception_utile import ControlNotFoundException


class Program:

    def __init__(self, app_path, app_dir, main_window_title):
        self.app_path = app_path
        self.app_dir = app_dir
        self.main_window_title = main_window_title

    def start_program(self):
        subprocess.Popen([self.app_path], cwd=self.app_dir)

    def connect_program(self):
        while True:
            try:
                self.app = Application(backend="uia").connect(title_re=self.main_window_title, timeout=10)
                print(f"链接：{self.main_window_title} 程序成功")
                return self.app
            except TimeoutError:
                print("连接失败，请检查地址是否配置正确")
                time.sleep(1)

    def operation_window(self, params, win_name=None):
        if win_name is None:
            win_name = self.main_window_title

        win = self.app.window(title_re=win_name)
        print(f"成功获取操作窗口：{win_name}")

        for item in params.get('input', []):
            target_control = win.child_window(title=item[0])
            if target_control.exists():
                self.set_text(target_control, item[1])
            else:
                print(f"未找到目标控件，参数为：{item[0]}")
                raise ControlNotFoundException("未找到控件")

        for item in params.get('click', []):
            target_control = win.child_window(title=item)
            if target_control.exists():
                # target_control.click_input()
                target_control.invoke()
            else:
                print(f"未找到目标控件，参数为：{item}")
                raise ControlNotFoundException("未找到控件")

    def set_text(self, control, text):
        siblings = control.parent().children()
        for i, sibling in enumerate(siblings):
            if sibling == control and i < len(siblings) - 1:
                sibling_edit = siblings[i + 1].set_text(text)
                return sibling_edit
        return None

# if __name__ == "__main__":
# APP_PATH = "path_to_your_app_executable"
# APP_DIR = "path_to_your_app_directory"
# MAIN_WINDOW = "main_window_title"
#
# automation = ProgramAutomation(APP_PATH, APP_DIR, MAIN_WINDOW)
#
# automation.start_program()
# automation.connect_program()
#
# params = {
#     'input': [('控件标题1', '文本1'), ('控件标题2', '文本2')],
#     'click': ['点击控件标题']
# }
# automation.operation_window(params)
