import pytest
from pytest_assume.plugin import assume
class TestAssert:
    """
    1. pytest.assume(断言)
    2. 先导入from pytest_assume.plugin import assume 再with assume:assert "william" in "cs"
    """
    def test_assert(self):
        with assume:assert "william" in "cs"
        pytest.assume(1+1==3)
        assert 1+1==2
        print("over")
        