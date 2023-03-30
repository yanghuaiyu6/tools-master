from repair.constants.constant_config import MAIN_WINDOW
from utile.program_utile import connect_program


class Click:
    def __init__(self, window_title):
        self.app = connect_program()  # ���ӳ���
        self.window = self.app.window(title=window_title)

    # ���������ť
    def left_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.invoke()

    # ����������루ѭ����
    def left_click_input_texts(self, control_parms, input_texts):
        for idx, control_spec in enumerate(control_parms):
            if idx < len(input_texts):
                control = self.window.child_window(**control_parms)
                control.click_input(button='left', double=False)
                control.type_keys(input_texts[idx])

    # ���˫��(��Ҫ����չʾ)
    def left_double_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.double_click_input()

    # ���˫������(��Ҫ����չʾ)
    def left_double_click_input_text(self, text, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.double_click_input()
        control.type_keys(text)

    # �Ҽ����
    def right_click(self, control_title, control_type, index=0):
        control = self.window.child_window(title=control_title, control_type=control_type, found_index=index)
        control.click_input(button='right', double=False)

    # �Ҽ������˵��Ĳ˵��������
    def right_click_menu(self, menu_control_title, control_type):
        # ͨ�����ڱ����ȡ���㴰��
        top_window = self.window.top_window()
        # ����Ҽ������Ĳ˵���
        menu_item = top_window.child_window(title=menu_control_title, control_type=control_type)
        # �������˵���
        menu_item.click_input(button='left')


if __name__ == "__main__":
    # window_title = 'Ŀ�괰�ڱ���'
    control_specs = [
        {'control_type': "DataItem", 'title': 'bus_0'},
        {'control_type': "DataItem", 'title': 'bus_1'}
    ]
    input_texts = ['�ı�1', '�ı�2', '�ı�3']
    demo = Click(window_title=MAIN_WINDOW)

    # ��1������������
    # demo.left_click("����", "Button")
    # demo.left_click("����", "Button")
    #
    # ��2�����������������ı�������ı��ؼ������ε�����룩

    # input_test = ["��һ������", "�ڶ�������"]
    # demo.left_click_input_texts(control_specs, input_test)

    # ��3��������˫��
    # demo.left_double_click("��һ������", "DataItem")
    #
    # ��4��������˫�������ı�����
    # input_text_for_double_click = '˫��������ı�'
    # demo.left_double_click_input_text("aaa", 'bus_0', "DataItem", )
    #
    # # ��5������Ҽ�����
    # demo.right_click("��Ŀ", "TreeItem")
