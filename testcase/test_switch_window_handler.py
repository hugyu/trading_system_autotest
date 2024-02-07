import allure
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
    """
    pytest --alluredir=UIreport  testcase/test_switch_window_handler.py
    将测试报告放在UIreport文件夹下
    allure serve UIreport 查看allure报告
    """
    # alllure的描述是窗口句柄
    @allure.description("窗口句柄")
    # 颗粒度越来越小
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_switch_window_handle(self,driver):
        # 测试的每一步
        with allure.step("登录"):
            LoginPage().login(driver,"jay")
            sleep(3)
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver,"外链")
            sleep(1)
        with allure.step("断言title"):
            title=ExternalLinkPage().goto_imooc(driver)
            print(title)
            assert title=="慕课网-程序员的梦工厂"
