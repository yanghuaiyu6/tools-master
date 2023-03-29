from pywinauto.findwindows import ElementAmbiguousError

from utile.constant_config import MAIN_WINDOW


# 右键点击方法
def right_click(app, title, control_type):
    try:
        win = app.window(title=MAIN_WINDOW)
        item = win.child_window(title=title, control_type=control_type).set_focus()
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
