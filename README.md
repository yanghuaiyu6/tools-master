# 需求说明

1.构型数的操作
2.菜单栏的操作
3.弹出窗口的操作
4.文本的输入

所有的操作有：
1.控件点击
（1）左键单击
（2）左键双击
（3）右键单击
2.文本输入
（1）点击控件之后输入
（2）点击控件之后输入循环输入

# 各个包的说明

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