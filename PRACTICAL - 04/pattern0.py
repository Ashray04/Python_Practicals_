def simple_modulo(a, b):
    if b == 0:
        return "Error: Divisor can't be Zero!"
    
    first_number = abs(a)
    second_number = abs(b)

    while first_number >= second_number:
        first_number -= second_number
    
    remainder = first_number

    if a < 0:
        remainder = remainder
    
    return remainder
aa=simple_modulo(-10,3)
bb=simple_modulo(-10,-3)
cc=simple_modulo(10,3)
print(aa)
print(bb)
print(cc)