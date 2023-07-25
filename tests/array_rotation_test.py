import unittest
from coding_puzzles import array_rotation


class TestArrayRotation(unittest.TestCase):

    def test_rotation_one(self):
        self.assertEqual([5, 1, 2, 3, 4], array_rotation.rotate([1, 2, 3, 4, 5], 1))

    def test_rotation_zero(self):
        self.assertEqual([1, 2, 3, 4, 5], array_rotation.rotate([1, 2, 3, 4, 5], 0))

    def test_rotation_three(self):
        self.assertEqual([3, 4, 5, 1, 2], array_rotation.rotate([1, 2, 3, 4, 5], 3))

    def test_rotation_five(self):
        self.assertEqual([1, 2, 3, 4, 5], array_rotation.rotate([1, 2, 3, 4, 5], 5))

    def test_rotation_six(self):
        self.assertEqual([5, 1, 2, 3, 4], array_rotation.rotate([1, 2, 3, 4, 5], 6))

    def test_rotation_small_array(self):
        self.assertEqual([4], array_rotation.rotate([4], 6))

    def test_rotation_large_k(self):
        self.assertEqual([6, 3, 4, 5], array_rotation.rotate([3, 4, 5, 6], 67725465))
