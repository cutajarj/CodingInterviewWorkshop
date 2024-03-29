import unittest

from coding_puzzles import sudoku_checker


class TestSudokuChecker(unittest.TestCase):
    def test_invalid_col(self):
        self.assertFalse(sudoku_checker.is_valid([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9]]))

    def test_invalid_row(self):
        self.assertFalse(sudoku_checker.is_valid([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                  [2, 2, 2, 2, 2, 2, 2, 2, 2],
                                                  [3, 3, 3, 3, 3, 3, 3, 3, 3],
                                                  [4, 4, 4, 4, 4, 4, 4, 4, 4],
                                                  [5, 5, 5, 5, 5, 5, 5, 5, 5],
                                                  [6, 6, 6, 6, 6, 6, 6, 6, 6],
                                                  [7, 7, 7, 7, 7, 7, 7, 7, 7],
                                                  [8, 8, 8, 8, 8, 8, 8, 8, 8],
                                                  [9, 9, 9, 9, 9, 9, 9, 9, 9]]))

    def test_invalid_box(self):
        self.assertFalse(sudoku_checker.is_valid([[6, 4, 2, 5, 8, 1, 3, 9, 7],
                                                  [5, 3, 1, 9, 4, 6, 8, 7, 2],
                                                  [2, 1, 4, 6, 3, 8, 7, 5, 9],
                                                  [1, 5, 6, 7, 9, 2, 4, 3, 8],
                                                  [7, 6, 8, 4, 5, 3, 9, 2, 1],
                                                  [9, 2, 3, 8, 6, 7, 5, 1, 4],
                                                  [4, 7, 9, 2, 1, 5, 6, 8, 3],
                                                  [8, 9, 7, 3, 2, 4, 1, 6, 5],
                                                  [3, 8, 5, 1, 7, 9, 2, 4, 6]]))

    def test_valid(self):
        self.assertTrue(sudoku_checker.is_valid([[5, 1, 2, 8, 4, 7, 9, 6, 3],
                                                  [4, 8, 6, 3, 2, 9, 7, 5, 1],
                                                  [9, 3, 7, 5, 6, 1, 2, 4, 8],
                                                  [3, 7, 4, 2, 5, 6, 1, 8, 9],
                                                  [1, 6, 5, 9, 8, 3, 4, 7, 2],
                                                  [2, 9, 8, 1, 7, 4, 6, 3, 5],
                                                  [8, 4, 3, 7, 9, 2, 5, 1, 6],
                                                  [7, 2, 1, 6, 3, 5, 8, 9, 4],
                                                  [6, 5, 9, 4, 1, 8, 3, 2, 7]]))