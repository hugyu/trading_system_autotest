from selenium.webdriver.common.by import By
from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap
class LeftMenuPage(LeftMenuBase,ObjectMap):
    def click_level_one_menu(self,driver,menu_name):
        """点击一级菜单

        Args:
            driver (_type_): 浏览器驱动
            menu_name (_type_): 菜单名称

        Returns:
            _type_: click事件
        """
        menu_xpath=self.level_one_menu(menu_name)
        return self.element_click(driver,By.XPATH,menu_xpath)
    def click_level_two_menu(self,driver,menu_name):
        """点击二级菜单

        Args:
            driver (_type_): 浏览器驱动
            menu_name (_type_): 菜单名称

        Returns:
            _type_: click事件
        """
        menu_xpath=self.level_two_menu(menu_name)
        return self.element_click(driver,By.XPATH,menu_xpath)
        