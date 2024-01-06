from time import sleep
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage
from config.driver_config import DriverConfig

class TestIframeBaiduMap:
    def test_iframe_baidu_map(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"iframe测试")
        sleep(1)
        # 先切进去 再切回来
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver,'首页')
        sleep(3)
if __name__ == '__main__':
    TestIframeBaiduMap().test_iframe_baidu_map()