import unittest

from coding_puzzles import sudoku_generater


class TestSudokuGenerator(unittest.TestCase):
    def test_rows(self):
        sodoku = sudoku_generater.generate_sudoku()
        numbers = set(range(1, 10))
        for r in range(9):
            row = set(sodoku[r])
            self.assertEqual(numbers, row)

    def test_cols(self):
        sodoku = sudoku_generater.generate_sudoku()
        numbers = set(range(1, 10))
        for c in range(9):
            col = set()
            for r in range(9):
                col.add(sodoku[r][c])
            self.assertEqual(numbers, col)

    def test_boxes(self):
        sudoku = sudoku_generater.generate_sudoku()
        numbers = set(range(1, 10))
        for outer_row in range(3):
            for outer_col in range(3):
                numbers_in_box = set()
                for row in range(3):
                    for col in range(3):
                        numbers_in_box.add(sudoku[outer_row * 3 + row][outer_col * 3 + col])
                self.assertEqual(numbers, numbers_in_box)
