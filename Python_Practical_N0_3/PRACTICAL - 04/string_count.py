def count (String,sub_str,truth_value) :
    count = 0
    length = len(sub_str)
    if(truth_value) :
        for i in range(0,len(String)) :
            s = String[i:i+length]
            if s == sub_str :
                count += 1
        return count
    else :
        i = 0
        while i <= len(String) - length:
            s = String[i:i + length]
            if s == sub_str:
                count += 1
                i += length
            else:
                i += 1
        return count
print(count("sgsgsgsg","sgs",False))