"""
构型树的创建
"""
import allure



# PROJECT_NAME = "项目名称"
# PRODUCT_NAME = "成品名称"
# PLUG_NAME = "插头名称"
# BUS_NAME = ["总线名称"]
# NODE_1394_NAME = "1394节点名称"
# ICD_NAME = "数据包"
# MSG_ID = "1H"


# 新建构型数（待完善）
@allure.story("新建完整的构型数")
def create_tree(program, click, project_name, product_name, plug_name, icd_name=None, msg_id=None):
    click.right_click(project_name, "TreeItem")
    click.right_click_menu("新建成品", "MenuItem")
    program.operation_window(win_name="创建新成品",
                             params={'input': [('名称：', product_name), ('ID', '测试1')], 'click': ["确定"]})

    click.right_click(product_name, "TreeItem")
    click.right_click_menu("新建插头组", "MenuItem")
    program.operation_window(win_name="创建新插头组",
                             params={'click': ["确定"]})

    click.right_click("插头组", "TreeItem")
    click.right_click_menu("新建Plug", "MenuItem")
    program.operation_window(win_name="创建新Plug",
                             params={'input': [('名称：', plug_name)], 'click': ["确定"]})

    click.right_click(plug_name, "TreeItem")
    click.right_click_menu("新建1394节点", "MenuItem")
    click.left_click("好的 Enter", "Button")

    # 创建总线（待完成）

    # click.right_click(plug_name, "TreeItem")
    # click.right_click_menu("新建1394节点", "MenuItem")
    # click.right_click("确定", "Button")
    # program.operation_window(win_name="创建新1394节点",
    #                          params={'input': [('名称：', '1394')], 'click': ["确定"]})
    #
    # click.right_click("输出", "TreeItem")
    # click.right_click_menu("新建ICD", "MenuItem")
    # click.right_click("属性信息", "TabItem")
    # program.operation_window(params={'input': [('数据包名称:', icd_name), ('消息ID:', msg_id)], 'click': ["域信息"]})
    # click.right_click("保存数据", "Button")

    pass


# 删除构型数
def delete_tree():
    pass


# 复制构型数
def copy_tree():
    pass


# 构型数的剪切
def cut_tree():
    pass
