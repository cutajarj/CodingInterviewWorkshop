# The input is a list of jumbled up sequential numbers start from 1 with one missing element.
# For example:
#     This is the sequence from 1 to 8: 1,2,3,4,5,6,7,8
# This is the same sequence jumbled up: 2,4,6,7,3,8,5,1
# We remove one random number (3)     : 2,4,6,7,8,5,1
# and feed it in to our function      : find_missing([2,4,6,7,8,5,1])
# should return 3
#
# Params:
#   Input 'numbers' is a list containing the range [1, n], where n is the length of list + 1
#   All numbers are unique (no duplicates)
#   Only one number is missing
#
# Returns:
#   Missing number
#
# Some more examples:
# find_missing([2,4,7,3,8,5,1]) should return 6
# find_missing([2,4,6,7,3,8,5]) should return 1
# find_missing([2,1,4]) should return 3
# find_missing([2,1,3]) should return 4
# find_missing([1]) should return 2
# find_missing([]) should return 1

def find_missing(numbers):
    return -1

