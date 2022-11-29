import unittest
from coding_puzzles import nesting


class TestNesting(unittest.TestCase):
    def test_simple_case(self):
        self.assertTrue(nesting.check_if_properly_nested("()"))

    def test_double_within(self):
        self.assertTrue(nesting.check_if_properly_nested("[()()]"))

    def test_bad_double_within(self):
        self.assertFalse(nesting.check_if_properly_nested("[(]()]"))

    def test_bad_overlap(self):
        self.assertFalse(nesting.check_if_properly_nested("[(])"))

    def test_triple_nested(self):
        self.assertTrue(nesting.check_if_properly_nested("[{()}]"))

    def test_triple_round_nested(self):
        self.assertTrue(nesting.check_if_properly_nested("((()))"))

    def test_bad_triple_round_nested(self):
        self.assertTrue(nesting.check_if_properly_nested("((())"))

    def test_bad_triple_nested(self):
        self.assertFalse(nesting.check_if_properly_nested("()]]"))

    def test_multi(self):
        self.assertTrue(nesting.check_if_properly_nested("()[]{}()[]{}"))

