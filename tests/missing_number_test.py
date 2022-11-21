import unittest
from coding_puzzles import missing_number


class TestMissingNumber(unittest.TestCase):
    def test_missing_6(self):
        self.assertEqual(6, missing_number.find_missing([2, 4, 7, 3, 8, 5, 1]))

    def test_missing_1(self):
        self.assertEqual(1, missing_number.find_missing([2, 4, 6, 7, 3, 8, 5]))

    def test_missing_4(self):
        self.assertEqual(4, missing_number.find_missing([2, 1, 3]))

    def test_missing_one_element(self):
        self.assertEqual(2, missing_number.find_missing([1]))

    def test_missing_empty(self):
        self.assertEqual(1, missing_number.find_missing([]))

    def test_missing_big(self):
        big = list(range(1, 30000))
        self.assertEqual(30000, missing_number.find_missing(big))
