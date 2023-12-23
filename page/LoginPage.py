from base.LoginBase import LoginBase
from selenium.webdriver.common.by import By

class LoginPage(LoginBase):
    def login_input_value(self,driver,input_placeholder,input_value):
        '''
        登录页输入值
        '''
        input_xpath=self.login_input(input_placeholder)
        print(input_xpath)
        return driver.find_element(By.XPATH,input_xpath).send_keys(input_value)
    def click_login(self,driver,button_name):
        '''
        点击登录
        '''
        button_xpath=self.login_button(button_name)
        return driver.find_element(By.XPATH,button_xpath).click()
        
