import time

from demo import connect_program

app = connect_program()
# 获取控件并右键
win = app.window(title='CC飞机飞管计算机全连接架构内总线数据流设计开发')
item = win.child_window(title="测试项目", control_type="TreeItem")
click = item.set_focus()
# 将焦点放在菜单项上并右键单击
# click.right_click_input()

# 右键点击控件
item.click_input(button='right')
time.sleep(2)


# 通过模拟键盘来实现菜单的选择
# app.top_window().type_keys('{DOWN}{DOWN}{DOWN}{ENTER}')
# 回到顶层窗口实现右键弹出菜单的点击
# app.top_window().child_window(title="新建成品", control_type="MenuItem").click_input(button='right')


def right_click_menu(app, menu_item_title, control_type):
    # 通过窗口标题获取顶层窗口
    top_window = app.top_window()
    # 点击右键弹出的菜单项
    menu_item = top_window.child_window(title=menu_item_title, control_type=control_type)
    # 左键点击菜单项
    menu_item.click_input(button='left')


if __name__ == '__main__':
    # 点击窗口标题为“测试窗口”的菜单项“新建成品”
    right_click_menu(app=app, menu_item_title="新建成品", control_type="MenuItem")
