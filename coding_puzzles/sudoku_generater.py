import random

sudoku = [[0 for i in range(9)] for j in range(9)]


def calculate_cell(row_number, col_number):
    if row_number > 8:
        return True
    rand_numbers = list(range(1, 10))
    random.shuffle(rand_numbers)
    for n in rand_numbers:
        if is_valid(n, row_number, col_number):
            sudoku[row_number][col_number] = n
            r, c = row_number, col_number + 1
            if c == 9:
                r, c = row_number + 1, 0
            if calculate_cell(r, c):
                return True
            else:
                sudoku[row_number][col_number] = 0
    return False


def is_valid(n, row_number, col_number):
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


def print_sudoku():
    for i in range(9):
        print(sudoku[i])


calculate_cell(0, 0)
print_sudoku()
