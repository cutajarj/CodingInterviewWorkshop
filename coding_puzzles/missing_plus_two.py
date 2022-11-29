# Complete the body of the function shown below
# The input of the function accepts one argument
#   a: Array of type integer of size between 2 and 2^31
#      the array contains a sequence starting from 0 and the following progression
#      [0,2,4,6,8,10 ... ]
# The array contains one missing number for example: [0,2,4,6,10,12] is missing 8
# Write a function that returns the missing number.
#
# Examples:
# a = [0,2,4,8,10], result = 6
# a = [0,2,4,6,10], result = 8
# a = [2,4,6], result = 0
#

def find_missing_number(numbers):
    start = 0
    finish = len(numbers) - 1
    mid = 0
    while finish - start >= 0:
        mid = start + (finish - start) // 2
        if numbers[mid] == mid * 2:
            start = mid + 1
        else:
            finish = mid - 1
    if numbers[mid] == mid * 2:
        return numbers[mid] + 2
    else:
        return numbers[mid] - 2
