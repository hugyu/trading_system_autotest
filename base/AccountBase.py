class AccountBase:
    def basic_info_avatar_input(self):
        """基本资料-个人头像

        Returns:
            xpath: 上传头像的xpath
        """
        return "//input[@type='file']"
    def basic_info_save_button(self):
        """基本资料-保存按钮

        Returns:
            xpath: 保存按钮的xpath
        """
        return "//span[text()='保存']/parent::button"