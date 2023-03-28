import time

from pywinauto import Application
from pywinauto.findwindows import ElementAmbiguousError


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


app = Application(backend="uia").connect(title_re="CC飞机飞管计算机全连接架构内总线数据流设计开发", timeout=1)
right_click(app, title="你好", control_type="TreeItem")
# 获取主窗口
win = app.window(title='CC飞机飞管计算机全连接架构内总线数据流设计开发')
# 获取“文件”菜单下的“打开”子菜单
file_menu_item = win.child_window(title="你好").wrapper_object().MenuItem("新建成品")
# 点击“打开”菜单项
file_menu_item.click_input()
