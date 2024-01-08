from base.LoginBase import LoginBase
from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
class LoginPage(LoginBase,ObjectMap):
    def login_input_value(self,driver,input_placeholder,input_value):
        '''
        登录页输入值
        '''
        input_xpath=self.login_input(input_placeholder)
        # return driver.find_element(By.XPATH,input_xpath).send_keys(input_value)
        return self.element_fill_value(driver,By.XPATH,input_xpath,input_value)
    def click_login(self,driver,button_name):
        '''
        点击登录
        '''
        button_xpath=self.login_button(button_name)
        # return driver.find_element(By.XPATH,button_xpath).click()
        return self.element_click(driver,By.XPATH,button_xpath)
    def login(self,driver,user):
        self.element_to_url(driver,"/login")
        username,password=GetConf().get_username_password(user)
        self.login_input_value(driver,"用户名",username)
        self.login_input_value(driver,"密码",password)
        self.click_login(driver,"登录")
    
    def login_assert(self,driver,img_name):
        """登录后判断头像是否一致

        Args:
            driver (_type_): 浏览器驱动
            img_name (string): 图片路径

        Returns:
            operation: 比对图片
        """
        return self.find_img_in_source(driver,img_name)
    
        
