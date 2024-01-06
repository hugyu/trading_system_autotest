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
    """
    @pytest.mark.bing
    # @pytest.mark.bing2
    def test_open_bing(self):
        driver=DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
    @pytest.mark.baidu
    def test_open_baidu(self):
        print("test_open_baidu")
        driver=DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
    @pytest.mark.google
    def test_open_google(self):
        driver=DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)