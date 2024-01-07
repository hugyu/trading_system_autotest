import pytest
from time import sleep
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.OrderPage import OrderPage

tab_list=["全部","待付款","待发货","运输中","待确认","待评价"]
class TestOrderBuy:
    """
    用例分开 解耦
    """
    @pytest.mark.parametrize("tab",tab_list)
    def test_order_buy(self,driver,tab):
        LoginPage().login(driver,"william")
        LeftMenuPage().click_level_one_menu(driver,"我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"已买到的宝贝")
        sleep(2)
        OrderPage().click_order_tab(driver,tab)
        sleep(2)
        
