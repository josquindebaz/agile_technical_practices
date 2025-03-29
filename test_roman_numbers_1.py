from unittest import TestCase

from roman_number_1 import Romaniser


def parameterize(arabic, expected):
    tester = Romaniser(arabic)

    assert tester.result == expected


class Test(TestCase):
    def test_romanise(self):
        expectations = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            11: "XI",
            14: "XIV",
            15: "XV",
            16: "XVI",
            19: "XIX",
            20: "XX",
            21: "XXI",
            24: "XXIV",
            29: "XXIX",
            30: "XXX",
            39: "XXXIX",
            40: "XL",
            41: "XLI",
            49: "XLIX",
            50: "L",
            90: "XC",
            99: "XCIX",
            100: "C",
            200: "CC",
            400: "CD",
            500: "D",
            700: "DCC",
            900: "CM",
            1000: "M",
            846: "DCCCXLVI",
            1999: "MCMXCIX",
            2008: "MMVIII"
        }

        for a, e in expectations.items():
            parameterize(a, e)
