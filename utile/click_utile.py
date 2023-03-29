from pywinauto.findwindows import ElementAmbiguousError

from utile.constant_config import MAIN_WINDOW


# 左键单机控件根据下标索引定位控件进行点击
def left_click_by_index(app, window_title, control_type, found_index=0):
    # 找到包含目标控件的窗口
    main_window = app.window(title=window_title)
    # 定位目标控件
    target_control = main_window.child_window(control_type=control_type, found_index=found_index)
    # 单击目标控件
    target_control.click_input()


# 左键单机控件根据控件类型和标题定位控件进行点击
def left_click_by_title_and_type(app, window_title, control_title, control_type):
    # 找到包含目标控件的窗口
    main_window = app.window(title=window_title)
    # 定位目标控件
    target_control = main_window.child_window(title=control_title, control_type=control_type)
    # 单击目标控件
    target_control.click_input()


# 右键点击方法
def right_click(app, title, control_type):
    try:
        win = app.window(title=MAIN_WINDOW)
        item = win.child_window(title=title, control_type=control_type).set_focus()
        item.click_input()
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


# 给已经有默认数据的单元格数据自定义赋值
def cell_input_text(app, window_title, control_title, input, control_type="DataItem"):
    # 找到包含表格的窗口
    main_window = app.window(title=window_title)
    # 定位类型的控件
    target_control = main_window.child_window(control_type=control_type, title=control_title)
    # 双击目标控件
    target_control.double_click_input()
    # 输入文本
    target_control.type_keys(input)
    # 模拟按下 Enter 键
    target_control.type_keys("{ENTER}")
