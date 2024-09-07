def bin_add(bin1, bin2):
    # Convert binary string to list of integers
    bin1 = list(map(int, bin1))
    bin2 = list(map(int, bin2))
    carry = 0
    for i in range(-1, -(len(bin1) + 1), -1):
        if bin1[i] == 1 and bin2[i] == 1:
            bin1[i] = 0 + carry
            carry = 1
        else:
            bin1[i] += bin2[i] + carry
            carry = 0
            if bin1[i] == 2:
                bin1[i] = 0
                carry = 1
    return (str(carry) + ''.join(map(str, bin1))) if carry else ''.join(map(str, bin1))

def bin_sub(bin1, bin2):
    valid_ele = ['-','b','0','1','B']
    
    # Validate the binary strings
    for i in bin1:
        if i not in valid_ele:
            return "Enter valid binary string"
    for i in bin2:
        if i not in valid_ele:
            return "Enter valid binary string"
    
    # Remove '0b', '0B', '-0b', or '-0B' prefixes
    if bin1.startswith(("-0b", "-0B")):
        bin1 = bin1[3:]
        b1 = 'n'
    elif bin1.startswith(("0b", "0B")):
        bin1 = bin1[2:]
        b1 = 'p'

    if bin2.startswith(("-0b", "-0B")):
        bin2 = bin2[3:]
        b2 = 'n'
    elif bin2.startswith(("0b", "0B")):
        bin2 = bin2[2:]
        b2 = 'p'
    
    # Ensure both binaries have the same length
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)
    
    # If one is negative and the other is positive, perform addition
    if (b1 == 'n' and b2 == 'p') or (b1 == 'p' and b2 == 'n'):
        if b1 == 'n':
            return '-' + bin_add(bin1, bin2)
        else:
            return bin_add(bin1, bin2)
    
    flag = 0
    
    # Ensure bin1 >= bin2 by swapping if necessary
    if bin1 < bin2:
        bin1, bin2 = bin2, bin1
        flag = 1

    # Convert binary strings to lists of integers
    bin1 = list(map(int, bin1))
    bin2 = list(map(int, bin2))
    
    # Perform binary subtraction with borrowing
    for i in range(-1, -(length + 1), -1):
        if bin1[i] >= bin2[i]:
            bin1[i] -= bin2[i]
        else:
            # Perform borrowing
            j = i - 1
            while j >= -length and bin1[j] == 0:
                bin1[j] = 1
                j -= 1
            bin1[j] = 0
            bin1[i] += 2 - bin2[i]

    result = ''.join(map(str, bin1)).lstrip('0')  # Remove leading zeros
    result = '0' if not result else result  # Ensure at least '0' is returned if the result is empty

    if flag:
        return '-0b' + result
    return '0b' + result

# Test the function
print(bin_sub('0B0', '0b1'))
