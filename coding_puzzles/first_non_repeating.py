# A string might contain characters that repeat. In this coding puzzle the solution
# needs to return the first character that doesn't repeat.
#
# Given an input string, return the first character from the left, that appears only once
# If all the characters in the input repeat, the function should return an empty string
# The function should be case-sensitive.
# Assume only english characters and normal punctuation is used.
# Examples:
# "seashore" should return "a" because "s" and "e" repeat
# "systematisation systems" should return "o"
# "fudgefudge" should return "" since all the characters repeat
# "fudGefudge" should return "G"

def find_first_non_repeating(text):
    table = [(0, 0)] * 256
    for i in range(len(text)):
        c = text[i]
        (count, position) = table[ord(c)]
        if count == 0:
            table[ord(c)] = (count + 1, i)
        else:
            table[ord(c)] = (count + 1, position)
    result, lowest_position = "", len(text)
    for i in range(len(table)):
        count, position = table[i]
        if position < lowest_position and count == 1:
            lowest_position = position
            result = chr(i)
    return result
