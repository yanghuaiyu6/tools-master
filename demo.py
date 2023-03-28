import time
import subprocess
from pywinauto.application import Application
from pywinauto.findwindows import ElementAmbiguousError

# 配置文件路径
# APP_PATH = r"E:\WJC\ICD\2023032701\ICMGROUP_Release_V120_20230327_1704_to_6\folder\ICMMain.exe"  # 程序启动地址
# APP_DIR = r"E:\WJC\ICD\2023032701\ICMGROUP_Release_V120_20230327_1704_to_6\folder"  # 将此替换为应用程序所在目录
APP_PATH = r"C:\Users\YANG\Desktop\赢瑞科技\软件产品\ICMGROUP_Release_V118_20221121_0927_to_6\ICMMain.exe"  # 程序启动地址
APP_DIR = r"C:\Users\YANG\Desktop\赢瑞科技\软件产品\ICMGROUP_Release_V118_20221121_0927_to_6"  # 将此替换为应用程序所在目录


# 启动程序
def start_program(app_path=APP_PATH, app_dir=APP_DIR):
    # 启动应用程序并设置工作目录
    subprocess.Popen([app_path], cwd=app_dir)


# 连接程序
def connect_program(title="CC飞机飞管计算机全连接架构内总线数据流设计开发"):
    # 等待应用程序加载
    while True:
        try:
            app = Application(backend="uia").connect(title_re=title, timeout=5)
            print("链接：" + title + "程序成功")
            return app
        except TimeoutError:
            print("连接失败，请检查地址是否配置正确")
            time.sleep(1)  # 等待1秒后重试连


# 连接操作程序的窗口，执行操作
def operation_window(app, params, win_name="CC飞机飞管计算机全连接架构内总线数据流设计开发"):
    # 链接应用程序
    win = app.window(title_re=win_name)
    print("成功获取操作窗口：" + win_name)

    # 首先处理所有的文本输入操作
    for item in params.get('input', []):
        target_control = win.child_window(title=item[0])
        if target_control.exists():
            # 设置文本
            set_text_next_to_control(target_control, item[1])
        else:
            print("未找到目标控件，参数为：" + item[0])
            try:
                # 在此处编写可能会引发“控件未找到异常”的代码
                raise ControlNotFoundException("未找到控件")
            except ControlNotFoundException as e:
                print(f"发生异常: {e}")

    # 然后处理所有的点击操作
    for item in params.get('click', []):
        target_control = win.child_window(title=item)
        if target_control.exists():
            # 执行点击操作
            target_control.invoke()
        else:
            print("未找到目标控件，参数为：" + item)
            try:
                # 在此处编写可能会引发“控件未找到异常”的代码
                raise ControlNotFoundException("未找到控件")
            except ControlNotFoundException as e:
                print(f"发生异常: {e}")


# 定位到标签后面的文本编辑框，传入控件
# 例：control = win.child_window(title="版本号", control_type="Text")
def set_text_next_to_control(control, text):
    siblings = control.parent().children()
    for i, sibling in enumerate(siblings):
        if sibling == control and i < len(siblings) - 1:
            sibling_edit = siblings[i + 1].set_text(text)
            return sibling_edit
    return None


# 自定义异常
class ControlNotFoundException(Exception):
    def __init__(self, message="控件未找到"):
        super().__init__(message)


# 右键点击方法
def right_click(app, title, control_type):
    try:
        win = app.window(title='CC飞机飞管计算机全连接架构内总线数据流设计开发')
        item = win.child_window(title=title, control_type=control_type).set_focus()
        # 将焦点放在菜单项上并右键单击
        item.right_click_input()
    except ElementAmbiguousError:
        print("找到多个菜单项，请更具体地指定控件")
    except Exception as e:
        print(f"发生异常: {e}")


# 右键弹出菜单的菜单点击方法
def right_click_menu(app, menu_item_title, control_type):
    # 通过窗口标题获取顶层窗口
    top_window = app.top_window()
    # 点击右键弹出的菜单项
    menu_item = top_window.child_window(title=menu_item_title, control_type=control_type)
    # 左键点击菜单项
    menu_item.click_input(button='left')


# 执行第一条测试
def main():
    # start_program()  # 启动程序
    app = connect_program()  # 连接程序
    # operation_window(app=app, win_name="项目选择框", params={'input': [], 'click': ["取消"]})  # 获取程序窗口，执行操作参数
    # operation_window(app=app, win_name="CC飞机飞管计算机全连接架构内总线数据流设计开发",
    #                  params={'input': [], 'click': ["项目", "新建项目"]})  # 获取程序窗口，执行操作参数
    # operation_window(app=app, win_name="创建项目",
    #                  params={'input': [('名称：', 'Hello！'), ('版本号', 'Hello, ICD!')], 'click': ["确定"]})
    # operation_window(app=app, win_name="CC飞机飞管计算机全连接架构内总线数据流设计开发",
    #                  params={'input': [], 'click': ["Hello！", "新建项目"]})
    right_click(app, title="测试项目", control_type="TreeItem")
    operation_window(app=app, win_name="新建成品", params={'click': ["新建成品"]})
    # 'input': [],


if __name__ == '__main__':
    main()
