import math


class Romaniser:
    def __init__(self, arabic):
        self.arabic = arabic
        self.result = ""

        decimals = ["I", "X", "C", "M", ""]
        quintals = ["V", "L", "D", ""]

        for i in range(3, -1, -1):
            self.compute(decimals[i], int(math.pow(10, i)), quintals[i], decimals[i + 1])

    def compute(self, decimal, multiplier, quintal, following_decimal):
        if self.arabic >= 9 * multiplier:
            self.substitute(decimal + following_decimal, 9 * multiplier)

        if self.arabic >= 5 * multiplier:
            self.substitute(quintal, 5 * multiplier)

        if self.arabic >= 4 * multiplier:
            self.substitute(decimal + quintal, 4 * multiplier)

        for i in range(0, int(self.arabic / multiplier)):
            self.substitute(decimal, multiplier)

    def substitute(self, letter, value):
        self.result += letter
        self.arabic -= value
