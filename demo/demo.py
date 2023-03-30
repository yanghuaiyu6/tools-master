from repair.constants.constant_config import APP_PATH, APP_DIR, MAIN_WINDOW
from utile.program import Program
from utile.click import Click

if __name__ == '__main__':
    # 启动程序
    program = Program(APP_PATH, APP_DIR, MAIN_WINDOW)
    # program.start_program()
    app = program.connect_program()
    # 激活控件
    click = Click(app)
    # program.operation_window(params={'input': [], 'click': ["取消"]}, win_name="项目选择框")
    # program.operation_window(params={'click': ["项目", "新建项目"]})
    # program.operation_window(win_name="创建项目",
    #                          params={'input': [('名称：', '测试项目1'), ('版本号', '测试1')], 'click': ["确定"]})

    # click.right_click("测试项目1", "TreeItem")
    # click.right_click_menu("新建成品", "MenuItem")
    # program.operation_window(win_name="创建新成品",
    #                          params={'input': [('名称：', '成品1'), ('ID', '测试1')], 'click': ["确定"]})
    #
    # click.right_click("成品1", "TreeItem")
    # click.right_click_menu("新建插头组", "MenuItem")
    # program.operation_window(win_name="创建新插头组",
    #                          params={'click': ["确定"]})
    #
    # click.right_click("插头组", "TreeItem")
    # click.right_click_menu("新建Plug", "MenuItem")
    # program.operation_window(win_name="创建新Plug",
    #                          params={'input': [('名称：', 'Plug1')], 'click': ["确定"]})
    #
    # click.right_click("Plug1", "TreeItem")
    # click.right_click_menu("新建1394节点", "MenuItem")
    #
    # click.left_click("好的 Enter", "Button")

    # 总线的操作
    # 后期增加
    click.right_click("自动Plug", "TreeItem")
    click.right_click_menu("新建1394节点", "MenuItem")
    click.right_click("确定", "Button")
    program.operation_window(win_name="创建新1394节点",
                             params={'input': [('名称：', '1394')], 'click': ["确定"]})
    #
    # click.right_click("输出", "TreeItem")
    # click.right_click_menu("新建ICD", "MenuItem")
    # click.right_click("属性信息", "TabItem")
    # program.operation_window(params={'input': [('数据包名称:', '1H'), ('消息ID:', '1H')], 'click': ["域信息"]})
    # click.right_click("保存数据", "Button")
