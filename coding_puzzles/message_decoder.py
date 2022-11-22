# A message containing only the letters from A to Z has been encoded in the following manner
# A -> 1
# B -> 2
# ...
# Z -> 26
# Given an encoded message we need to find the number of different ways it can be decoded
# For example the message "19173" can be decoded in 4 ways:
# "1 9 1 7 3" -> "A I A G C"
# "1 9 17 3" -> "A I Q C"
# "19 1 7 3" -> "S A G C"
# "19 17 3" -> "A Q C"
# We cannot use "1 91 7 3" because "91" is more than 26
# The message "11106" can be decoded in 2 ways:
# "1 1 10 6" -> "A A J F"
# "11 10 6" -> "K J F"
# We cannot use "1 11 06" because "06" cannot be mapped into 'F' since "6" is different from "06"
# Other examples:
# number_of_ways_to_decode("11") Should return 2
# number_of_ways_to_decode("216") Should return 3
# number_of_ways_to_decode("100") Should return 0
# number_of_ways_to_decode("001") Should return 0
#
# Constraints:
# 1 <= len(encoding) <= 100
# encoding contains only digits and may contain leading zero(s).


def number_of_ways_to_decode(encoding):
    return number_of_ways(encoding, {})


def number_of_ways(encoding, cache):
    if encoding in cache:
        return cache[encoding]
    if encoding[0] == "0":
        return 0
    if len(encoding) == 1:
        return 1

    choose_two = 0
    if int(encoding[:2]) <= 26:
        choose_two = 1 if len(encoding[2:]) == 0 else number_of_ways(encoding[2:], cache)
    result = number_of_ways(encoding[1:], cache) + choose_two
    cache[encoding] = result
    return result


if __name__ == '__main__':
    print(number_of_ways_to_decode("11106"))
    print(number_of_ways_to_decode("19173"))


