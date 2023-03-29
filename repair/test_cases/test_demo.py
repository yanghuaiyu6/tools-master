import logging
import pytest


# 每个测试模块（一个.py文件）只会执行一次初始化和清理操作
@pytest.fixture(scope="module")
def app():
    # 打开应用程序，并获取应用程序对象
    # app = Application().start("应用程序路径")
    yield app

    # 在测试用例执行完后，关闭应用程序
    app.kill()


def test_case1(app):
    # 在测试用例中，可以直接使用app来操作应用程序对象
    # app.top_window().child_window(title="按钮1").click()
    assert True


def test_case2(app):
    # 在测试用例中，可以直接使用app来操作应用程序对象
    # app.top_window().child_window(title="按钮2").click()
    assert True


def test_case3(app):
    # 在测试用例中，可以直接使用app来操作应用程序对象
    # app.top_window().child_window(title="按钮2").click()
    assert True


def test_case4(app):
    # 在测试用例中，可以直接使用app来操作应用程序对象
    # app.top_window().child_window(title="按钮2").click()
    assert True
