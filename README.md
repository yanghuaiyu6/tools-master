# 一、需求说明

## 1.进入软件

## 2.执行用例

- 2.1 用例读取

待定

### 2.2 执行步骤

- 2.2.1 按照目的进行分类：

（1）新数据的创建 ：从0-1
（2）旧数据的操作 ：直接导入数据

- 2.2.2 操作的类型分类：

（0）定位窗口
（1）鼠标左键单击
（2）鼠标左键单击输入文本（多个文本控件，依次点击输入）
（3）鼠标左键双击
（4）鼠标左键双击进行文本输入
（5）鼠标右键单击
（6）文本的输入

## 3.执行结果

## 4.输出报告

## 5.系统集成

# 二、涉及到的控件分类

## 1.菜单栏控件类型

    MenuItemControlTypeId 

## 2.工具栏控件类型

    ToolBarControlTypeId ：空白处
    ButtonControlTypeId ：按钮
    CheckBoxControlTypeId ：复选框
    ToolTipControlTypeId ：提示控件（无用）

工具栏展开之后的浮动窗口没法使用

## 3.项目展示区域

    TabControlTypeId ：空白处
    TabItemControlTypeId ：选项卡项目

## 4.构型树区域

    EditControlTypeId ：编辑（搜索框）
    TreeItemControlTypeId ：树项目
    TreeControlTypeId ：构型树空白处

右键：
MenuItemControlTypeId ：菜单项目

## 5.主操作区

    PaneControlTypeId ：空白主操纵区域
    TabItemControlTypeId ：选项卡项目，（上面的页签和下面的页签）
    EditControlTypeId ：编辑
    ButtonControlTypeId ：按钮
    TextControlTypeId ：文本（标签）
    ComboBoxControlTypeId ：组合框
    CheckBoxControlTypeId ：复选框
    TreeItemControlTypeId ：ICD数据包中每个单元格和整行都是此控件
    DataItemControlTypeId ：发送接收节点
    ScrollBarControlTypeId ：滚动条

## 6.提示栏

    CheckBoxControlTypeId 
    DataItemControlTypeId 
    TableControlTypeId ：表头
    ButtonControlTypeId 
    TreeItemControlTypeId 
    ThumbControlTypeId ：缩略图（放大缩小窗口）

## 7.操作窗口

    ComboBoxControlTypeId ：组合框
    EditControlTypeId ：编辑
    ButtonControlTypeId 
    TextControlTypeId ：文本
    TabItemControlTypeId 
    PaneControlTypeId ：窗格
    SpinnerControlTypeId ：日期选择
    RadioButtonControlTypeId：开关
    TreeItemControlTypeId ：项目选择
    DataItemControlTypeId ：总线列表
    MenuItemControlTypeId 
    TabControlTypeId ：选项卡
    RadioButtonControlTypeId ：单选按钮
    CheckBoxControlTypeId ：复选框

# 三、各个包的说明

config：包含用于配置测试工具的文件和模块，例如 settings.py 文件，其中包含了工具的默认设置和参数。
logs：包含用于记录测试过程和结果的模块和工具，例如 log_util.py 模块，其中包含了用于写日志文件的函数和类。
reports：包含用于生成测试报告的模块和工具，例如 report_util.py 模块，其中包含了用于生成 HTML 测试报告的函数和类。
test_cases：包含用于测试的测试用例代码，例如 test_case1.py、test_case2.py、test_case3.py 等文件。
test_data：包含用于测试的测试数据文件，例如 test_data1.csv、test_data2.json、test_data3.xml 等文件。
utils：包含用于测试的工具类和函数，例如 file_util.py、string_util.py、time_util.py 等文件，其中包含了用于读写文件、处理字符串和日期时间的函数和类。
requirements.txt：包含用于安装依赖项的 Python 包列表。
执行以下命令，将当前环境中所有的依赖包及其版本信息输出到requirements.txt文件中：
```pip freeze > requirements.txt```

README.md：包含有关工具使用和安装说明的文档。

# 方法的说明

click_input() 更接近实际的鼠标操作，而 invoke() 则直接触发控件的特定操作。
set_focus() 可以确保在执行与控件相关的操作之前，控件处于活动状态并准备好接收输入。

# 脚本的使用方法

1.启动软件
2.激活控件
3.进行调用

# pytest使用介绍
1.失败重试：使用 @pytest.mark.flaky(reruns=n) 装饰器，可以指定在测试用例失败时重试的次数。例如：
```angular2html
import pytest

@pytest.mark.flaky(reruns=3)
def test_addition():
    assert 1 + 1 == 3

```
2.跳过测试：使用 @pytest.mark.skip 或 @pytest.mark.xfail 装饰器，可以跳过测试用例或标记预期失败的测试用例。例如：
```angular2html
import pytest

@pytest.mark.skip(reason="test is not ready")
def test_addition():
    assert 1 + 1 == 3

@pytest.mark.xfail(reason="test is expected to fail")
def test_division():
    assert 1 / 0 == 2

```
3.参数化测试：使用 @pytest.mark.parametrize 装饰器，可以将多组参数传递给同一个测试用例。例如：
```angular2html
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 4, 7), (5, 6, 11)])
def test_addition(a, b, expected):
    assert a + b == expected

```
4.@pytest.fixture() 是 pytest 中用于定义测试前置条件（setup）和后置条件（teardown）的装饰器。
    前置条件是在测试用例运行之前需要执行的代码，例如创建测试环境、初始化测试数据等。
    后置条件是在测试用例运行之后需要执行的代码，例如清理测试环境、关闭数据库连接等。
    定义 @pytest.fixture() 装饰器的函数，可以在测试用例中通过函数名作为参数来调用该函数， 从而获得测试前置条件和后置条件的功能。
```angular2html
import pytest

@pytest.fixture(scope="function")
def setup():
    # 测试前置条件
    print("setup")
    yield
    # 测试后置条件
    print("teardown")

def test_case1(setup):
    print("test_case1")
    assert 1 + 1 == 2

def test_case2(setup):
    print("test_case2")
    assert 2 + 2 == 4

```
    setup 函数中的 yield 语句用于分隔前置条件和后置条件。
    scope 参数指定前置条件和后置条件的作用范围。默认值为 function，表示只在单个测试用例函数运行期间有效，其他可选值还有 module、class 和 session 等。

# Allure的使用说明
## 1.分类
    Allure 提供的注解 @Epic、@Feature、@Story 和 @Severity 来为测试指定分类。具体来说：
    @Epic：代表测试用例或测试套件的顶层层次结构，通常用于描述产品或项目的整体目标或需求。
    @Feature：代表一类测试，通常对应于产品或项目中的一个功能或者一组功能。
    @Story：代表一个具体的测试场景，通常对应于用户故事或者用例。
    @Severity：代表测试的重要程度或严重程度。
## 2.用例描述
    @Title：为测试用例添加标题。
    @Description：为测试用例添加描述信息。
    @Severity：为测试用例添加严重程度标签，例如：critical、blocker、minor等。
    @Issue：为测试用例关联缺陷管理系统中的问题/问题单。
    @Link：为测试用例添加链接，例如：测试计划、需求规格说明等。
    @Attachment：将附件附加到测试报告中，例如：日志、截图等。
    @allure.suite注解只能用于函数或方法上，不能用于类。同时，每个测试用例只能属于一个Suites套件，不能同时属于多个Suites套件。
使用这些注解，可以使测试报告更加清晰、易读、易理解，帮助测试团队更好地进行测试管理和缺陷跟踪。
Suites套件是用来对测试用例进行逻辑分组和分类的，可以将一些相关的测试用例归为同一套件，方便查看和管理测试结果。
Suites套件可以根据不同的维度来进行分组，比如按照功能模块、业务流程、测试类型等进行分组。
在Allure报告中，可以通过Suites套件来查看测试用例的分组情况，并且可以查看每个套件的测试结果统计信息。















