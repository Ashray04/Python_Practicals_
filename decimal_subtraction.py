def decimal_subtraction(num1, num2):
    result = ''
    borrow = 0
    
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i >= 0 or j >= 0:
        if i >= 0:
            digit1 = ord(num1[i]) - ord('0')
        else:
            digit1 = 0
        
        if j >= 0:
            digit2 = ord(num2[j]) - ord('0')
        else:
            digit2 = 0
        
        digit1 = digit1 - borrow
        
        if digit1 < digit2:
            digit1 = digit1 + 10
            borrow = 1
        else:
            borrow = 0
        
        difference = digit1 - digit2
        character_difference = chr(difference + ord('0'))
        
        result = character_difference + result
        
        i = i - 1
        j = j - 1
    
    if borrow == 1:
        result = '-' + result
    
    return result

num1 = "123"
num2 = "98"
result = decimal_subtraction(num1, num2)
print(result)

