class LeftMenuBase:
    def level_one_menu(self,menu_name):
        """
        一级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/ancestor::li"
    def level_two_menu(self,menu_name):
        """
        二级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='"+menu_name+"']/parent::li"
        