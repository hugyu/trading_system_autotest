import time
from selenium.common.exceptions import ElementNotVisibleException,WebDriverException
class ObjectMap:
    def element_get(self,driver,locate_type,locate_expression,timeout=10,must_be_visible=False):
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
        start_ms=time.time()*1000
        # 设置的结束时间
        stop_ms=start_ms+(timeout*1000)
        for x in range(int(timeout*10)):
            # 查找元素
            try:
                element=driver.find_element(locate_type,locate_expression)
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
                now_ms=time.time()*1000
                if(now_ms>=stop_ms):
                    break
            time.sleep(0.1)
            raise ElementNotVisibleException("元素定位失败，定位方式："+locate_type+" 定位表达式：" + locate_expression)
    def wait_for_ready_state_complete(self,driver,timeout=30):
        """获取页面状态

        Args:
            driver (_type_): 浏览器驱动
            timeout (int, optional): 时间间隔. Defaults to 30.

        Returns:
            bool: 是否加载完成
        """
        #开始时间
        start_ms=time.time()*1000
        #设置结束时间
        stop_ms=start_ms+(timeout*1000)
        for x in range((int(timeout*10))):
            try:
                ready_state=driver.execute_script("return document.readyState")
            except WebDriverException:
                #如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面全部加载完成，返回True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms=time.time()*1000
                # 如果超时了 就跳出
                if now_ms>=stop_ms:
                    break
                time.sleep(0.1)
            raise Exception("打开网页时，页面元素在%s秒仍然没有完全加载"%timeout)
    def element_disapper(self,driver,locate_type,locate_expression,timeout=30):
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
            start_ms=time.time()*1000 
            # 结束时间
            stop_ms =start_ms + (timeout*1000)
            for x in range(int(timeout*10)):
                try:
                    element=driver.find_element(locate_type,locate_expression)
                    if element.is_displayed():
                        now_ms=time.time()*1000
                        if(now_ms>=stop_ms):
                            break
                        time.sleep(0.1)
                        
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式："+locate_type+"\n定位表达式："+locate_expression)
        else:
            pass
    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
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
                    element = driver.find_element(by=locate_type, value=locator_expression)
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
            raise ElementNotVisibleException("元素定位失败，定位方式： " + locate_type + " 定位表达式: " + locator_expression)
        else:
            pass

    