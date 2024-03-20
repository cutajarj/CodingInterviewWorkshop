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