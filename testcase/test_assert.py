class TestAssert:
    def test_assert(self):
        # == != < > <= >=
        assert "william"=="william"
        assert 2!=5
        assert 0<1
        assert 2>1
        # in ,not in
        assert "william" in "william cs"
        assert "wil" not in "cs"
        # true false
        assert 1
        assert (9<10) is True
        assert not False
        