from unittest import TestCase

from stats_calculator import Stats

exercise_series = [6, 9, 15, -2, 92, 11]


class TestMinimum(TestCase):
    def test_minimum_of_two(self):
        stats = Stats([2, 1])
        expected = 1

        result = stats.minimum

        self.assertEqual(expected, result)

    def test_minimum_of_three(self):
        stats = Stats([11, 9, 15])
        expected = 9

        result = stats.minimum

        self.assertEqual(expected, result)

    def test_minimum_with_negative_number(self):
        stats = Stats([11, 9, -2])
        expected = -2

        result = stats.minimum

        self.assertEqual(expected, result)

    def test_minimum_of_negative_numbers(self):
        stats = Stats([11, -9, -2])
        expected = -9

        result = stats.minimum

        self.assertEqual(expected, result)

    def test_minimum_of_exercise(self):
        stats = Stats(exercise_series)
        expected = -2

        result = stats.minimum

        self.assertEqual(expected, result)


class TestMaximum(TestCase):
    def test_maximum_of_two(self):
        stats = Stats([2, 1])
        expected = 2

        result = stats.maximum

        self.assertEqual(expected, result)

    def test_maximum_of_three(self):
        stats = Stats([11, 9, 15])
        expected = 15

        result = stats.maximum

        self.assertEqual(expected, result)

    def test_maximum_with_negative_number(self):
        stats = Stats([11, 9, -2])
        expected = 11

        result = stats.maximum

        self.assertEqual(expected, result)

    def test_maximum_of_negative_numbers(self):
        stats = Stats([-9, -2])
        expected = -2

        result = stats.maximum

        self.assertEqual(expected, result)

    def test_maximum_of_exercise(self):
        stats = Stats(exercise_series)
        expected = 92

        result = stats.maximum

        self.assertEqual(expected, result)


class TestNumber(TestCase):
    def test_number_with_one(self):
        stats = Stats([0])
        expected = 1

        result = stats.number

        self.assertEqual(expected, result)

    def test_number_with_negative(self):
        stats = Stats([-1, 2])
        expected = 2

        result = stats.number

        self.assertEqual(expected, result)

    def test_number_of_exercise(self):
        stats = Stats(exercise_series)
        expected = 6

        result = stats.number

        self.assertEqual(expected, result)


class TestAverage(TestCase):
    def test_average_with_one(self):
        stats = Stats([10])
        expected = 10

        result = stats.average

        self.assertEqual(expected, result)

    def test_average_with_two(self):
        stats = Stats([2, 4])
        expected = 3

        result = stats.average

        self.assertEqual(expected, result)

    def test_average_to_float(self):
        stats = Stats([1, 2, 7])
        expected = 3.3333333333333335

        result = stats.average

        self.assertEqual(expected, result)

    def test_average_of_exercise(self):
        stats = Stats(exercise_series)
        expected = 21.833333333333332

        result = stats.average

        self.assertEqual(expected, result)
