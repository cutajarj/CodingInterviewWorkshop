# Complete the body of the function shown below
# The input of the function accepts one argument
#   text: A string of length 2 characters or more containing a
#         combination of only the characters "(", "{", "[", "]", "}", ")"
#
# The function should return true iff the string is properly nested
#
# Examples:
# text = "[()()]", result = true
# text = "[(]()]", result = false
# text = "[{()}]", result = true
# text = "((()))", result = true
# text = "[(])", result = false
# text = "((())", result = false
# text = "()]]", result = false
# text = "()[]{}()[]{}", result = true

def check_if_properly_nested(text):
    stack = []
    for c in text:
        if c in ["[", "(", "{"]:
            stack.append(c)
        elif c == "]" and stack.pop() != "[":
            return False
        elif c == "}" and stack.pop() != "{":
            return False
        elif c == ")" and stack.pop() != "(":
            return False
    return len(stack) == 0
