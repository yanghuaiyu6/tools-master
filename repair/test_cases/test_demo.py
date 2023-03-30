import allure
import pytest


@allure.epic("顶层描述")
@allure.feature("模块名称")
@allure.story("场景描述")
@allure.title("标题名称")
@allure.severity("严重程度")
@allure.suite("测试套件")
def test_case1(setup):
    print("可以写明步骤，会在报告的日志中进行查看")
    print("test_case1")
    assert 1 + 1 == 2


@pytest.fixture(scope="function")
def setup():
    # 测试前置条件
    print("前置条件")
    yield
    # 测试后置条件
    print("后置条件")
