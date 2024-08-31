def integer_to_roman(num):
    # Define Roman numeral mappings
    roman_numerals = [
        (100000, 'C̅'),
        (90000, 'XC̅'),
        (50000, 'L̅'),
        (40000, 'XL̅'),
        (10000, 'X̅'),
        (9000, 'MX̅'),
        (5000, 'V̅'),
        (4000, 'MV̅'),
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    if num <= 0:
        raise ValueError("Number must be greater than 0")
    if num >= 100000:
        raise ValueError("Number out of range (1 - 99999)")
    result = ""
    for value, numeral in roman_numerals:
        while num >= value:
            result += numeral
            num -= value
    return result
# Convert 59 to Roman numeral
print(integer_to_roman(19999)) #Output:LIX