from unittest import TestCase

from boolean_rapsody import calculator


def parameterize(case, expected):
    result = calculator(case)
    assert result == expected


class Test(TestCase):
    def test_calculator(self):
        expectations = {
            "TRUE": True,
            "FALSE": False,
            "NOT TRUE": False,
            "TRUE AND FALSE": False,
            "TRUE AND TRUE": True,
            "TRUE OR FALSE": True,
            "TRUE OR TRUE OR TRUE AND FALSE": True,
            "TRUE OR FALSE AND NOT FALSE": True,
            "(TRUE OR TRUE OR TRUE) AND FALSE": False,
            "NOT (TRUE AND TRUE)": False

        }

        for case, expectation in expectations.items():
            parameterize(case, expectation)
