def ends_with_a(text):
    return "Accepted" if q0(text) else "Rejected"
    
def q0(text):
    if(text[0]) == 'b':
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    elif(text[0]) == 'a':
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    else:
        return False
        
def q1(text):
    if(text[0]) == 'a':
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    elif(text[0]) == 'b':
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    else:
        return False

print(ends_with_a("babababbababbaba"))