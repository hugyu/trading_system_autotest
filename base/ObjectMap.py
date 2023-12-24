import time
from selenium.common.exceptions import ElementNotVisibleException
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
            
        