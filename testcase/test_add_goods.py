import pytest
from time import sleep
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from config.driver_config import DriverConfig


class TestAddGoods:
    @pytest.fixture()
    def driver(self):
        get_driver=DriverConfig().driver_config()
        yield get_driver
        get_driver.quit()
    def test_add_goods_001(self,driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(driver,
                                  goods_title="新增商品测试hgy",
                                  goods_details="新增商品测试详情hgy",
                                  goods_num=1,
                                  goods_pic_list=["goods.jpg"],
                                  goods_price=123,
                                  goods_status="上架",
                                  bottom_button_name="提交")
        sleep(3)
if __name__ == '__main__':
    TestAddGoods().test_add_goods_001()