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

    print(is_valid([[5, 1, 2, 8, 4, 7, 9, 6, 3],
                    [4, 8, 6, 3, 2, 9, 7, 5, 1],
                    [9, 3, 7, 5, 6, 1, 2, 4, 8],
                    [3, 7, 4, 2, 5, 6, 1, 8, 9],
                    [1, 6, 5, 9, 8, 3, 4, 7, 2],
                    [2, 9, 8, 1, 7, 4, 6, 3, 5],
                    [8, 4, 3, 7, 9, 2, 5, 1, 6],
                    [7, 2, 1, 6, 3, 5, 8, 9, 4],
                    [6, 5, 9, 4, 1, 8, 3, 2, 7]]))