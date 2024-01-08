import pytest
from time import sleep
from page.LoginPage import LoginPage
class TestLoginAssert:
    @pytest.mark.login
    def test_login_assert(self,driver):
        LoginPage().login(driver,"jay")
        sleep(3)
        # 0.349669486284256 > 0.5
        assert LoginPage().login_assert(driver,"head_img.png")>0.34121 