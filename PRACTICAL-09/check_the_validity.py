def check_validity(text: str):
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in text:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack or bracket_pairs[stack.pop()] != char:
                return (0, 1)
    
    if stack:
        return (0, 1)

    return (1, 1)

text1 = "(<)>"
text2 = "+()"
text3 = "{1}"
text4 = ")("
text5 = "([{}])"

print(check_validity(text1))  # (0, 1)
print(check_validity(text2))  # (1, 1)
print(check_validity(text3))  # (1, 1)
print(check_validity(text4))  # (0, 1)
print(check_validity(text5))  # (1, 1)