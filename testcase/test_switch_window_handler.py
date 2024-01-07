from time import sleep
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
class TestWindowHandle:
    def test_switch_window_handle(self,driver):
        LoginPage().login(driver,"jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"外链")
        sleep(1)
        title=ExternalLinkPage().goto_imooc(driver)
        print(title)
