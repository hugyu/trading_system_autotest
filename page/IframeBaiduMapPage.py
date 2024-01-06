from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase
class IframeBaiduMapPage(IframeBaiduMapBase,ObjectMap):
    def get_baidu_map_search_button(self,driver):
        """获取百度地图的搜索按钮

        Args:
            driver (_type_): 浏览器驱动

        Returns:
            element: 按钮
        """
        button_xpath=self.search_button()
        return self.element_get(driver,By.XPATH,button_xpath)
    def switch_2_baidu_map_iframe(self,driver):
        """切换到百度地图iframe

        Args:
            driver (_type_): 浏览器驱动

        Returns:
            event: 切换到百度地图iframe
        """
        iframe_xpath=self.baidu_map_iframe()
        return self.switch_into_frame(driver,By.XPATH,iframe_xpath)
    def iframe_out(self,driver):
        """从iframe切换到主页面

        Args:
            driver (_type_): 浏览器驱动

        Returns:
            event: 切换到主页面
        """
        return self.switch_from_iframe_to_content(driver)