from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.AccountBase import AccountBase
from common.tools import get_img_path
class AccountPage(ObjectMap,AccountBase):
    def upload_avatar(self,driver,img_name):
        """上传个人头像

        Args:
            driver (_type_): 浏览器驱动
            img_name (string): 图片名称

        Returns:
            event: 上传图片
        """
        img_xpath=get_img_path(img_name)
        upload_xpath=self.basic_info_avatar_input()
        return self.upload(driver,By.XPATH,upload_xpath,img_xpath)
    def click_save(self,driver):
        """点击保存

        Args:
            driver (_type_): 浏览器驱动

        Returns:
            event: 点击保存按钮
        """
        button_xpath=self.basic_info_save_button()
        return self.element_click(driver,By.XPATH,button_xpath)