def base(text,text_base,output_base):
    number=int(text,text_base)     #convert in integer
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #all possible digit characters for base up to 36
    
    if number == 0:       #if input is 0 means text or text_base
        return "0"
    
    result = ""
    while number > 0:       #input should not be zero
        result = digits[number % output_base] + result    #formula
        number //= output_base
    return result

print(base("1234", 10, 34))
print(base("1011110", 2, 23))
print(base("11100", 2, 4))
print(base("10011", 2, 15))
print(base("111", 8, 18))
print(base("111101",2,7))
print(base("111100",10,27))
print(base("01111",10,25))
