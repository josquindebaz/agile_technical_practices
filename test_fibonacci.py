from unittest import TestCase

from fibonacci import fibo


class Test(TestCase):
    def test_range(self):
        cases = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34
        ]

        for case, expected in enumerate(cases):
            result = fibo(case)

            self.assertEqual(result, expected)
