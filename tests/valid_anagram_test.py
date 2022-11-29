import unittest
from coding_puzzles import valid_anagram


class TestValidAnagram(unittest.TestCase):
    def test_brainy(self):
        self.assertTrue(valid_anagram.is_anagram("binary", "brainy"))

    def test_car(self):
        self.assertFalse(valid_anagram.is_anagram("rat", "car"))

    def test_tab(self):
        self.assertFalse(valid_anagram.is_anagram("BAT", "tab"))

    def test_fairy_tales(self):
        self.assertTrue(valid_anagram.is_anagram("rail safety", "fairy tales"))

    def test_they_see(self):
        self.assertTrue(valid_anagram.is_anagram("the eyes", "they see"))

    def test_bad_credit(self):
        self.assertTrue(valid_anagram.is_anagram("debit card", "bad credit"))

    def test_cannot_aim(self):
        self.assertTrue(valid_anagram.is_anagram("action man", "cannot aim"))

    def test_empty(self):
        self.assertTrue(valid_anagram.is_anagram("", ""))

    def test_bad_length(self):
        self.assertFalse(valid_anagram.is_anagram("batt", "tab"))

