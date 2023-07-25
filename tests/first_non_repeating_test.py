import unittest
from coding_puzzles import first_non_repeating


class TestFirstNonRepeating(unittest.TestCase):
    def test_seashore(self):
        self.assertEqual("a", first_non_repeating.find_first_non_repeating("seashore"))

    def test_fudgefudge(self):
        self.assertEqual("", first_non_repeating.find_first_non_repeating("fudgefudge"))

    def test_long_string(self):
        self.assertEqual("g", first_non_repeating.find_first_non_repeating("learning javascript is pretty lame"))

    def test_empty_str(self):
        self.assertEqual("", first_non_repeating.find_first_non_repeating(""))

    def test_upper_lower(self):
        self.assertEqual("A", first_non_repeating.find_first_non_repeating("aaaAaaa"))

    def test_space(self):
        self.assertEqual(" ", first_non_repeating.find_first_non_repeating("fudge fudge"))

