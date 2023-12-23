class LoginBase:
    def login_input(self,input_placeholder):
        """
        登录用户名，密码输入值
        """
        return "//input[@placeholder='"+input_placeholder+"']"
    def login_button(self,button_name):
        '''
        登录按钮
        '''
        return "//span[text()='"+button_name+"']/parent::button"
    