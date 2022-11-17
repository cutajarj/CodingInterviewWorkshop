import unittest
from coding_puzzles import missing_number


class TestStringMethods(unittest.TestCase):
    def test_missing_6(self):
        self.assertEqual(missing_number.find_missing([2, 4, 7, 3, 8, 5, 1]), 6)

    def test_missing_1(self):
        self.assertEqual(missing_number.find_missing([2, 4, 6, 7, 3, 8, 5]), 1)

    def test_missing_4(self):
        self.assertEqual(missing_number.find_missing([2, 1, 3]), 4)

    def test_missing_one_element(self):
        self.assertEqual(missing_number.find_missing([1]), 2)

    def test_missing_empty(self):
        self.assertEqual(missing_number.find_missing([]), 1)

