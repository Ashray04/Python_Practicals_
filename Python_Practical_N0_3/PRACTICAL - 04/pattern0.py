def modulo (a,b) :
    if(b == 0) :
        return "Error Divisor can't be Zero!"
    first_number = abs(a)
    second_number = abs(b)
    mod = 0;
    sum = 0;
    while (sum<first_number) : 
        sum += second_number
    if(sum==first_number) :
            return 0
    else :
            mod = first_number-sum+second_number
    if(a > 0 and b > 0) :
        return mod;
    elif(a>0 and b<0 ) :
        return mod-second_number;
    elif(a < 0 and b < 0) :
        return mod - 2*mod;
    elif(a<0 and b>0) :
        return mod-second_number+(2*abs(mod-second_number))
    else :
        return 0