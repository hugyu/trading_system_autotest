import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException,NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from common.yaml_config import GetConf


class ObjectMap:
    # 获取基准地址
    url = GetConf().get_url()

    def element_get(self,
                    driver,
                    locate_type,
                    locate_expression,
                    timeout=10,
                    must_be_visible=False):
        """获取元素

        Args:
            driver (_type_): 浏览器驱动
            locate_type (_type_): 定位方式
            locate_expression (_type_): 定位表达式
            timeout (int, optional): 超时时间. Defaults to 10.
            must_be_visible (bool, optional): 元素是否可见. Defaults to False.

        Raises:
            Exception: 元素没有显示
            ElementNotVisibleException: 元素不可见

        Returns:
            元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(locate_type, locate_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 是可见的
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if (now_ms >= stop_ms):
                    break
            time.sleep(0.1)
            raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type +
                                             " 定位表达式：" + locate_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """获取页面状态

        Args:
            driver (_type_): 浏览器驱动
            timeout (int, optional): 时间间隔. Defaults to 30.

        Returns:
            bool: 是否加载完成
        """
        #开始时间
        start_ms = time.time() * 1000
        #设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range((int(timeout * 10))):
            try:
                ready_state = driver.execute_script(
                    "return document.readyState")
            except WebDriverException:
                #如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面全部加载完成，返回True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了 就跳出
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
            raise Exception("打开网页时，页面元素在%s秒仍然没有完全加载" % timeout)

    def element_disapper(self,
                         driver,
                         locate_type,
                         locate_expression,
                         timeout=30):
        """等待页面消失

        Args:
            driver (_type_): 浏览器驱动
            locate_type (_type_): 定位方式
            locate_expression (_type_): 定位表达式
            timeout (int, optional): 超时时间. Defaults to 10.

        Raises:
            Exception: 元素没有消失

        Returns:
            bool:元素消失
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(locate_type,
                                                  locate_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if (now_ms >= stop_ms):
                            break
                        time.sleep(0.1)

                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + "\n定位表达式：" +
                            locate_expression)
        else:
            pass

    def element_appear(self,
                       driver,
                       locate_type,
                       locator_expression,
                       timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type,
                                                  value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if (now_ms >= stop_ms):
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("元素定位失败，定位方式： " + locate_type +
                                             " 定位表达式: " + locator_expression)
        else:
            pass

    def element_to_url(self,
                       driver,
                       url,
                       locate_type_disappear=None,
                       locator_expression_disappear=None,
                       locate_type_appear=None,
                       locator_expression_appear=None):
        """
        跳转地址
        :param driver:浏览器驱动
        :param url:跳转的地址
        :param locate_type_disappear:等待页面元素消失的定位方式
        :param locator_expression_disappear:等待页面元素消失的定位表达式
        :param locate_type_appear:等待页面元素出现的定位方式
        :param locator_expression_appear:等待页面元素出现的定位表达式
        :return:
        """
        try:
            # 基准的地址加上拼接的地址
            driver.get(self.url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待元素消失
            self.element_disappear(driver, locate_type_disappear,
                                   locator_expression_disappear)
            # 跳转地址后等待元素出现
            self.element_appear(driver, locate_type_appear,
                                locator_expression_appear)
        except Exception as e:
            print("跳转地址出现异常，异常原因:%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:定位方式
        :param locator_expression:定位表达式
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 页面中未找到该元素
            return False

    def element_fill_value(self,
                           driver,
                           locate_type,
                           locator_expression,
                           fill_value,
                           timeout=30):
        """
        元素填值
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param fill_value:填的值
        :param timeout:超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(driver,
                                      locate_type=locate_type,
                                      locator_expression=locator_expression,
                                      timeout=timeout)
        try:
            # 清除元素中原有的值
            element.clear()
        except StaleElementReferenceException:  # 如果元素没有刷新出来，就对元素进行捕获
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入的值改成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout)
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")

        return True
