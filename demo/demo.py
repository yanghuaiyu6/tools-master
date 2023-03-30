from repair.common.tree_config import create_tree
from repair.constants.constant_config import APP_PATH, APP_DIR, MAIN_WINDOW, PROJECT_NAME, PRODUCT_NAME, MSG_ID, \
    ICD_NAME, NODE_1394_NAME, BUS_NAME, PLUG_NAME
from utile.program import Program
from utile.click import Click

if __name__ == '__main__':
    # 启动程序
    program = Program(APP_PATH, APP_DIR, MAIN_WINDOW)
    # program.start_program()
    app = program.connect_program()
    # 激活控件
    click = Click(app)
    #
    # program.operation_window(params={'input': [], 'click': ["取消"]}, win_name="项目选择框")
    # program.operation_window(params={'click': ["项目", "新建项目"]})
    # program.operation_window(win_name="创建项目",
    #                          params={'input': [('名称：', '测试项目1'), ('版本号', '测试1')], 'click': ["确定"]})

    create_tree(program, click, project_name="测试项目1", product_name=PRODUCT_NAME,
                plug_name=PLUG_NAME, icd_name=BUS_NAME, msg_id=NODE_1394_NAME)

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
