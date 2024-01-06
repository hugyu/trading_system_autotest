from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase
class OrderPage(ObjectMap,OrderBase):
    def click_order_tab(self,driver,tab_name):
        """点击订单tab栏按钮

        Args:
            driver (_type_): 浏览器驱动
            tab_name (string): tab名称

        Returns:
            event: tab点击事件
        """
        tab_xpath=self.order_tab(tab_name)
        return self.element_click(driver,By.XPATH,tab_xpath)
    
    