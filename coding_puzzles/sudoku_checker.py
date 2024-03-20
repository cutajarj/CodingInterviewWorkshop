# Implement this function that accepts a 2d array containing integers between 1 and 9, of size 9x9
# The function should return true if the input is a valid sudoku-
# A sudoku is valid if:
#   each separate row and column does not contain duplicate numbers
#   each of the 9, 3x3 boxes don't contain duplicate numbers
#   only numbers from 1 to 9 are allowed in each cell
# Assume:
# The input is a 9x9 2d array of type integer
# each element in the array is in the range [1,9]

def is_valid(sudoku):
    numbers_rows = [1] * 9
    numbers_cols = [1] * 9
    numbers_box = [1] * 9
    for i in range(9):
        for j in range(9):
            n_row = sudoku[j][i]
            numbers_rows[n_row - 1] = 0
            n_col = sudoku[i][j]
            numbers_cols[n_col - 1] = 0
            r, c = (i % 3 * 3) + j % 3, (i // 3 * 3) + j // 3
            n_box = sudoku[r][c]
            numbers_box[n_box] = 0
        if sum(numbers_rows) + sum(numbers_cols) + sum(numbers_box) != 0:
            return False

    return True


if __name__ == '__main__':
    print(is_valid([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9]]))
