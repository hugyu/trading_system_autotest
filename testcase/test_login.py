from time import sleep
from page.LoginPage import LoginPage

class TestLogin():
    def test_login(self,driver):
        LoginPage().login(driver,"jay")
        sleep(3)        
