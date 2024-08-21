def practical_five(s, style):
    result = ""
    if style == 'C':  #To upper
        for char in s:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
    elif style == 'L':  #to lower
        for char in s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    elif style == 'R':  #in reverse manner
        for char in s:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            elif 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    elif style == 'U':  # Zigzag
        for i in range(len(s)):
            char = s[i]
            if i % 2 == 0:
                if 'A' <= char <= 'Z':
                    result += chr(ord(char) + 32)
                else:
                    result += char
            else:
                if 'a' <= char <= 'z':
                    result += chr(ord(char) - 32)
                else:
                    result += char
    return result
s = "Ashray"
print(practical_five(s, 'C'))  # All Capital case
print(practical_five(s, 'L'))  # All Lower case
print(practical_five(s, 'R'))  # Reverse Case
print(practical_five(s, 'U'))  # Zigzag Case
