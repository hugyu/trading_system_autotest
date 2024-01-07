import pytest
from config.driver_config import DriverConfig

"""
开始--发现测试用例为driver--进入conftest执行driver--生成get_driver打开浏览器
--用例执行完毕--get_driver返回conftest的driver中--关闭浏览器--结束
"""
"""
conftest可以跨文件调用
conftest的文件名是固定的
就近原则 同级目录 上级目录
conftest不能被其他文件导入
conftest 可以设置多个pytest内置的钩子函数
"""
@pytest.fixture()
def driver():
    get_driver=DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()