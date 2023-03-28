import time
import win32gui
import win32api
import pywinauto
from pywinauto.timings import wait_until

from demo import right_click, connect_program

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
# 回到顶层窗口实现点击
app.top_window().child_window(title="新建成品", control_type="MenuItem").click_input(button='right')
