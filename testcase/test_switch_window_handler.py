from time import sleep
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
class TestWindowHandle:
    """
    pytest -s -q testcase/test_switch_window_handler.py --html=report.html
    --html=report.html 在根目录生成测试报告 名为report.html 文件与样式分离
    --self-contained-html 生成一个html文件里面包含css样式
    """
    def test_switch_window_handle(self,driver):
        LoginPage().login(driver,"jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"外链")
        sleep(1)
        title=ExternalLinkPage().goto_imooc(driver)
        print(title)
