import random

# Implement this function to populate the 2d array with a random valid sudoku
# Everytime you run this program a different sudoku should be printed
# A sudoku is valid if:
#   each separate row and column does not contain duplicate numbers
#   each of the 9, 3x3 boxes don't contain duplicate numbers
#   only numbers from 1 to 9 are allowed in each cell
def calculate_cell(row_number, col_number, sudoku):
    return False


def is_valid(n, row_number, col_number, sudoku):
    for i in range(9):
        if sudoku[row_number][i] == n or sudoku[i][col_number] == n:
            return False
    st_row = (row_number // 3) * 3
    st_col = (col_number // 3) * 3
    for i in range(st_row, st_row + 3):
        for j in range(st_col, st_col + 3):
            if sudoku[i][j] == n:
                return False
    return True


def generate_sudoku():
    sudoku = [[0 for i in range(9)] for j in range(9)]
    calculate_cell(0, 0, sudoku)
    return sudoku


if __name__ == '__main__':
    sudoku = generate_sudoku()
    for i in range(9):
        print(sudoku[i])
