from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage

class TestLogin():
    def test_login(self):
        driver=DriverConfig.driver_config()
        LoginPage().login(driver,"jay")
        sleep(3)        
if __name__ == '__main__':
    TestLogin().test_login()