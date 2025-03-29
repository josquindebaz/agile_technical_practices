from unittest import TestCase

from leap_year import leap_year


class Test(TestCase):
    def test_leap_year_2001(self):
        for year in range(2001, 2003):
            result = leap_year(year)

            assert result == False

    def test_leap_year_1996(self):
        result = leap_year(1996)

        assert result == True

    def test_leap_year_2000(self):
        result = leap_year(2000)

        assert result == True

    def test_leap_year_1900(self):
        for year in range(1700, 1900, 100):
            result = leap_year(year)

            assert result == False
