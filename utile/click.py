from repair.constants.constant_config import MAIN_WINDOW
from utile.program_utile import connect_program


class Click:

    def __init__(self):
        self.app = connect_program()  # 连接程序
        self.window = self.app.window()

    # 左键单击按钮（后端执行）
    def left_click_hide(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.invoke()

    # 左键单击按钮（基于界面）
    def left_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.click_input(button='left')

    # 左键单击输入（循环）
    def left_click_input_texts(self, control_parms, input_texts):
        for idx, control_spec in enumerate(control_parms):
            if idx < len(input_texts):
                control = self.window.child_window(**control_parms)
                control.click_input(button='left', double=False)
                control.type_keys(input_texts[idx])

    # 左键双击(需要界面展示)
    def left_double_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.double_click_input()

    # 左键双击输入(需要界面展示)
    def left_double_click_input_text(self, text, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.double_click_input()
        control.type_keys(text)

    # 右键点击
    def right_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.click_input(button='right', double=False)

    # 右键弹出菜单的菜单点击方法
    def right_click_menu(self, menu_control_title, control_type):
        # 通过窗口标题获取顶层窗口
        top_window = self.app.top_window()
        # 点击右键弹出的菜单项
        menu_item = top_window.child_window(title=menu_control_title, control_type=control_type)
        # 左键点击菜单项
        menu_item.click_input(button='left')

# 以下是执行案例
# if __name__ == "__main__":
#     window_title = '目标窗口标题'
# demo = Click(window_title=MAIN_WINDOW)
#     control_specs = [
#         {'control_type': "DataItem", 'title': 'bus_0'},
#         {'control_type': "DataItem", 'title': 'bus_1'}
#     ]
#     input_texts = ['文本1', '文本2', '文本3']

# （1）鼠标左键单击
# demo.left_click("项目", "MenuItem")
# demo.left_click("新建项目", "MenuItem")
#
# （2）鼠标左键单击输入文本（多个文本控件，依次点击输入）

# input_test = ["第一条总线", "第二条总线"]
# demo.left_click_input_texts(control_specs, input_test)

# （3）鼠标左键双击
# demo.left_double_click("第一条总线", "DataItem")
#
# （4）鼠标左键双击进行文本输入
# input_text_for_double_click = '双击输入的文本'
# demo.left_double_click_input_text("aaa", 'bus_0', "DataItem", )
#
# # （5）鼠标右键单击
# demo.right_click("项目", "TreeItem")
# demo.right_click_menu("新建成品", "MenuItem")
