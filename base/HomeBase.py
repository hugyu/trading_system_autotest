class HomeBase:
    def wallet_switch(self):
        '''
        首页的钱包开观
        '''
        return "//span[contains(@class,'switch')]"
    def logo(self):
        '''
        进入系统后左上角的logo
        '''
        return "//div[contains(text(),'二手')]"
    def welcome(self):
        '''
        首页欢迎您回来
        '''
        return "//span[starts-with(text(),'欢迎')]"
    def show_date(self):
        '''
        首页显示日期
        '''
        return "//div[text()='我的日历']/following-sibling::div"
    def home_user_avatar(self):
        '''
        首页用户头像大图
        '''
        return "//span[contains(text(),'欢迎')]/parent::div/preceding-sibling::div//img"
    def home_user_avatar2(self):
        '''
        首页用户头像大图2
        '''
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"
    