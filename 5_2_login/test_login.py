from config.driver_config import DriverConfig
from selenium.webdriver.common.by import By
config = DriverConfig()
driver=config.driver_config()
driver.get('http://www.tcpjwtester.top')

# 用户名
driver.find_element(By.XPATH,"//input[@placeholder='用户名']").send_keys('周杰伦')
#密码
driver.find_element(By.XPATH,"//input[@placeholder='密码']").send_keys('123456')
#点击登录
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/button').click()

