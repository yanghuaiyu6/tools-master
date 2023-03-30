import subprocess
import time
from pywinauto import Application


class ControlNotFoundException(Exception):
    print("������")


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
                print(f"���ӣ�{self.main_window_title} ����ɹ�")
                return self.app
            except TimeoutError:
                print("����ʧ�ܣ������ַ�Ƿ�������ȷ")
                time.sleep(1)

    def operation_window(self, params, win_name=None):
        if win_name is None:
            win_name = self.main_window_title

        win = self.app.window(title_re=win_name)
        print(f"�ɹ���ȡ�������ڣ�{win_name}")

        for item in params.get('input', []):
            target_control = win.child_window(title=item[0])
            if target_control.exists():
                self.set_text(target_control, item[1])
            else:
                print(f"δ�ҵ�Ŀ��ؼ�������Ϊ��{item[0]}")
                raise ControlNotFoundException("δ�ҵ��ؼ�")

        for item in params.get('click', []):
            target_control = win.child_window(title=item)
            if target_control.exists():
                target_control.click_input()
            else:
                print(f"δ�ҵ�Ŀ��ؼ�������Ϊ��{item}")
                raise ControlNotFoundException("δ�ҵ��ؼ�")

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
    #     'input': [('�ؼ�����1', '�ı�1'), ('�ؼ�����2', '�ı�2')],
    #     'click': ['����ؼ�����']
    # }
    # automation.operation_window(params)
