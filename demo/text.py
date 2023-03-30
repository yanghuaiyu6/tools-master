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

    # program.operation_window(params={'click': ["测试项目1", "新建成品"]}, win_name="项目选择框")
    click.right_click("测试项目1", "TreeItem")
    click.right_click_menu("新建成品", "TreeItem")
