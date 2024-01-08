import cv2
from common.tools import get_project_path, sep
class FindImg:
    def img_imread(self, img_path):
        """
        读取图片方法
        :param img_path: 图片路径
        :return:
        """
        return cv2.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片的方法
        :param source_path:原图路径
        :param search_path:需要查找图片的路径
        :return:
        """
        # 读取原图
        img_src = self.img_imread(source_path)
        # 读取需要查找的图片
        img_sch = self.img_imread(search_path)
        result = cv2.matchTemplate(img_src, img_sch, cv2.TM_CCOEFF_NORMED)
        _, confidence, _, _ = cv2.minMaxLoc(result)
        return confidence

if __name__ == '__main__':
    source_path = get_project_path() + sep(["img",  "source.jpg"], add_sep_before=True)
    search_path = get_project_path() + sep(["img",  "source.jpg"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)
