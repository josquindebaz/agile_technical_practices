from unittest import TestCase

from fizzbuzz import fizzbuzz


class Test(TestCase):
    def test_when1(self):
        result = fizzbuzz(1)

        assert result == "1"

    def test_when2(self):
        result = fizzbuzz(2)

        assert result == "2"

    def test_when3(self):
        result = fizzbuzz(3)

        assert result == "fizz"

    def test_when4(self):
        result = fizzbuzz(4)

        assert result == "4"

    def test_when5(self):
        result = fizzbuzz(5)

        assert result == "buzz"

    def test_when15(self):
        result = fizzbuzz(15)

        assert result == "fizzbuzz"
