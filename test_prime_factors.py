from unittest import TestCase

from prime_factors import get_prime_factors


def parameterize(number, expected):
    result = get_prime_factors(number)

    assert result == expected


class Test(TestCase):
    def test_get_prime_factors(self):
        expectations = {
            1: [1],
            2: [2],
            3: [3],
            4: [2, 2],
            6: [2, 3],
            7: [7],
            8: [2, 2, 2],
            9: [3, 3],
            10: [2, 5],
            11: [11],
            12: [2, 2, 3],
            15: [3, 5]
        }

        for case, expectation in expectations.items():
            parameterize(case, expectation)
