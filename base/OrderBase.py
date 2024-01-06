class OrderBase:
    def order_tab(self,tab_name):
        """tab的xpath

        Args:
            tab_name (string): tab名称

        Returns:
            _type_: tab的xpath
        """
        return "//div[@role='tab' and text()='"+tab_name+"']"