from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DriverConfig:
    def driver_config():
        """
        浏览器驱动
        :return:
        """
        # 实例化谷歌浏览器设置方法
        options = Options()
        # 不自动关闭浏览器
        options.add_experimental_option("detach", True)
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL的错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式(不打开浏览器后台运行)
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")  # gpu加速
        options.add_argument("--no-sandbox")  # 进入沙箱
        options.add_argument("--disable-dev-shm-usage")  # 防止测试用例过多内存溢出

        # service = Service(executable_path="path/to/chromedriver") # 指定chromedriver路径
        driver = webdriver.Chrome(options=options)  # 自动更新最新浏览器版本的ChromeDriver
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
