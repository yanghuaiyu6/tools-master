from repair.constants.constant_config import MAIN_WINDOW
from utile.click_utile import right_click_menu, right_click
from utile.program_utile import start_program, connect_program, operation_window


# start_program()  # 启动程序
app = connect_program()  # 连接程序
if __name__ == '__main__':
    # operation_window(app=app, win_name="项目选择框", params={'input': [], 'click': ["取消"]})
    # 获取程序窗口，执行操作参数
    # operation_window(app=app, win_name=MAIN_WINDOW, params={'input': [], 'click': ["项目", "新建项目"]})
    # 创建项目，传入参数
    # operation_window(app=app, win_name="创建项目",
    #                  params={'input': [('名称：', '自动项目1'), ('版本号', '自动1')], 'click': ["确定"]})
    # 控制右键点击相应的控件
    right_click(app, title="项目", control_type="TreeItem")
    # 弹出项目层菜单栏进行点击的操作
    right_click_menu(app=app, menu_item_title="新建成品", control_type="MenuItem")
    # 定位到创建新成品窗口中
    operation_window(app=app, win_name="创建新成品",
                     params={'input': [('名称：', '自动成品'), ('ID', '自动id')], 'click': ["确定"]})

    # 控制右键点击成品层控件
    right_click(app, title="自动成品", control_type="TreeItem")
    right_click_menu(app=app, menu_item_title="新建插头组", control_type="MenuItem")
    operation_window(app=app, win_name="创建新插头组", params={'click': ["确定"]})

    # 控制右键点击插头组层控件
    right_click(app, title="插头组", control_type="TreeItem")
    right_click_menu(app=app, menu_item_title="新建Plug", control_type="MenuItem")
    operation_window(app=app, win_name="创建新Plug", params={'input': [('名称：', '自动Plug')], 'click': ["确定"]})

    # 控制右键点击插头层控件
    right_click(app, title="自动Plug", control_type="TreeItem")
    right_click_menu(app=app, menu_item_title="新建1394节点", control_type="MenuItem")
    # 弹窗处理
    right_click_menu(app=app, menu_item_title="好的 Enter", control_type="Button")

    # 添加总线
    operation_window(app=app, win_name=MAIN_WINDOW, params={'click': ["新增", "新增"]})
    # # 双击输入文本内容
    # cell_input_text(app=app, window_title=MAIN_WINDOW, control_title="bus_0", control_type="DataItem",
    #                 input="1394CC总线")
    # cell_input_text(app=app, window_title=MAIN_WINDOW, control_title="bus_1", control_type="DataItem",
    #                 input="1394CCDL总线")
    # 下拉框的选择
    # left_click_by_index(app=app, window_title=MAIN_WINDOW, control_type="DataItem", found_index=1)
    # 选择总线类型（待定）
    # right_click_menu(app=app, menu_item_title="1553总线", control_type="ListItem")

    # 保存总线
    # left_click_by_title_and_type(app=app, window_title=MAIN_WINDOW, control_type="Button", control_title="保存")

    # 继续新建总线节点
    # 控制右键点击插头层控件
    right_click(app, title="自动Plug", control_type="TreeItem")
    right_click_menu(app=app, menu_item_title="新建1394节点", control_type="MenuItem")
    # 弹窗处理
    right_click_menu(app=app, menu_item_title="确定", control_type="Button")
    operation_window(app=app, win_name="创建新1394节点", params={'input': [('名称：', '自动')], 'click': ["确定"]})

    # 输出节点新建ICD数据包
    right_click(app, title="输出", control_type="TreeItem")
    right_click_menu(app=app, menu_item_title="新建ICD", control_type="MenuItem")
    # 弹窗处理
    right_click(app, title="属性信息", control_type="TabItem")
    operation_window(app=app, params={'input': [('数据包名称:', '1H'), ('消息ID:', '1H')], 'click': ["域信息"]})
    # 保存ICD
    right_click(app, title="保存数据", control_type="Button")
