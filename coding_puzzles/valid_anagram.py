# Complete the body of the function shown below
# The input of the function accepts two arguments
#   s: A string of length 0 or more characters
#   t: A string of length 0 or more characters
#
# The function should return true iff the strings are anagrams of each other
# Characters are case sensitive.
# Assume that the string is not UTF.
#
# Examples:
# s = "binary", t = "brainy" result = true
# s = "rat", t = "car" result = false
# s = "BAT", t = "tab" result = false (different case)
# s = "rail safety", t = "fairy tales" result = true
# s = "the eyes", t = "they see" result = true
# s = "debit card", t = "bad credit" result = true
# s = "action man", t = "cannot aim" result = true
# s = "", t = "" result = true
# s = "batt", t = "tab" result = false
def is_anagram(s, t):
    table = [0] * 256
    for c in s:
        table[ord(c)] += 1
    for c in t:
        table[ord(c)] -= 1
        if table[ord(c)] < 0:
            return False
    return len(s) == len(t)

