import unittest

from services.FibService import FibService
from repository.MyDatabase import MSSqlDatabase


class TestFibService(unittest.TestCase):
    def test_get_combination_sum(self):
        actual = FibService(MSSqlDatabase()).get_combination_sum(10)
        expected = [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [2, 8], [5, 5]]
        self.assertEqual(actual, expected)

    def test_get_fibonacci_series(self):
        actual = FibService(MSSqlDatabase()).get_fibonacci_series(10)
        expected = [2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(actual, expected)

    def test_unique_combination_series_sum(self):
        series = [2, 3, 5, 8, 13, 21, 34]
        actual = FibService(MSSqlDatabase()).unique_combination_series_sum(series, 10)
        expected = [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [2, 8], [5, 5]]
        self.assertEqual(actual, expected)
