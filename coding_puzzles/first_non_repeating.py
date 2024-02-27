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
