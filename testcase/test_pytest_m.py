from time import sleep
from config.driver_config import DriverConfig
import pytest
class TestPytestMClass:
    # 装上装饰器 给标记 可以给多个标记
    """
    -m 只运行被标记的测试用例
    pytest -m "baidu or bing" testcase
    pytest -m "baidu and bing" testcase
    pytest -m "not baidu" testcase
    pytest -m "baidu and not bing" testcase
    -k 模糊匹配文件名
    pytest -k pytest 文件名中有pytest
    pytest -k Class  类名中有Class
    pytest -k open   方法名中有open
    -s 可以在终端中打印调试信息
    pytest -s -m baidu
    -v 显示执行的详细信息
    --collect-only 只收集用例 不执行
    pytest --collect-only
    -q 显示简洁的执行信息
    pytest -q -m  baidu
    -n 指定打开几个浏览器
    pytest -n 2
    pytest -n auto 根据电脑的cpu核来打开浏览器个数
    pytest -n auto --dist=loadscope 同一文件的测试用例有先后关系可能会导致第二个用例失败 不会同时执行
    """
    
    """
    fixture的用途:包裹测试用例
    @pytest.fixture()
    将fixture名作为用例的函数
    作用范围:session class module function
    """ 
    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class 级别，我只执行一次")
    @pytest.fixture(scope="function")
    def driver(self):
        get_driver=DriverConfig().driver_config()
        return get_driver
    
    @pytest.mark.bing
    # @pytest.mark.bing2
    def test_open_bing(self,driver,scope_class):
        # driver=DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
    @pytest.mark.baidu
    def test_open_baidu(self,driver,scope_class):
        print("test_open_baidu")
        # driver=DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
    @pytest.mark.google
    def test_open_google(self,driver,scope_class):
        # driver=DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)