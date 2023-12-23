class OrderTabBase:
    def A(self,tab_name):
        """
        作业
        :param tab_name:
        :return:
        """
        return "//div[@class='el-card__body']//div[text()='"+tab_name+"']"