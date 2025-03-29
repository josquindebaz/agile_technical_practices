class Stats:
    def __init__(self, values):
        self.number = 0
        self.sum = 0
        self.minimum = None
        self.maximum = None

        for value in values:
            if not self.minimum or value < self.minimum:
                self.minimum = value

            if not self.maximum or value > self.maximum:
                self.maximum = value

            self.number += 1
            self.sum += value

    @property
    def average(self):
        return self.sum / self.number
