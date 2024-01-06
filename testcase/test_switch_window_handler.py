from time import sleep
from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
class TestWindowHandle:
    def test_switch_window_handle(self):
        driver=DriverConfig().driver_config()
        LoginPage().login(driver,"jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"外链")
        sleep(1)
        title=ExternalLinkPage().goto_imooc(driver)
        print(title)
if __name__ == '__main__':
    TestWindowHandle().test_switch_window_handle()