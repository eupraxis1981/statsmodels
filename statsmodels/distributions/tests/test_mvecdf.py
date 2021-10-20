from statsmodels.distributions import MVECDF


class TestMVECDF:
    def test_init(self):
        assert MVECDF()
