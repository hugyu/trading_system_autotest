import random
import pytest
class TestRerun:
    """
    pytest-rerunfailures 失败重跑插件
    pytest testcase/test_rerun.py --reruns 5 --reruns-delay1
    --reruns 5 最多重跑5次
    --reruns-delay1 失败了间隔1s再跑
    或者采用pytest mark来使用
    """
    # @pytest.mark.flaky(reruns=5,reruns_delay=1)
    def test_rerun(self):
        num=random.randint(1,3)
        print("num:",num)
        if(num!=1):
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")