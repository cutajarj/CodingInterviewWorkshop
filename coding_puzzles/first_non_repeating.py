
def find_first_non_repeating(text):
    table = [0] * 256
    for c in text:
        table[ord(c)] += 1
    result = ""
    for c in text:
        if table[ord(c)] == 1:
            result = c
            break
    return result
