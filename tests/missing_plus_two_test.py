import unittest
from coding_puzzles import missing_plus_two


class TestMissingPlusTwo(unittest.TestCase):
    def test_missing_six(self):
        self.assertEqual(6, missing_plus_two.find_missing_number([0,2,4,8,10]))

    # a = [0,2,4,6,10], result = 8
    def test_missing_eight(self):
        self.assertEqual(8, missing_plus_two.find_missing_number([0,2,4,6,10]))

        # a = [2,4,6], result = 0
    def test_missing_zero(self):
        self.assertEqual(0, missing_plus_two.find_missing_number([2,4,6]))

    # checks no linear algorithm was used
    def test_missing_large(self):
        a = list(range(0, 19999998, 2))
        a.append(20000000)
        self.assertEqual(19999998, missing_plus_two.find_missing_number(a))
