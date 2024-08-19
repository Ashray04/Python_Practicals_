def print_pattern (line) :
    list=[]
    if(line<1) :
        print("Invalid Number");
    else :
        z=int(line);
        if(z-line) :
            print("Invalid Number Please Enter Valid Number");
        line=int(line)
        total_number_of_spaces = 2*(line+2);
        number_of_spaces = 0;
        star = 0;
        number = " ";
        #to print the upper part without base
        for i in range (1,line+2) :
            print(" "*(total_number_of_spaces - i*2) + "+" + " " * (number_of_spaces) + str(number) + " " * (number_of_spaces) +"+" * (star));
            if(i==1) :
                star = star+1;
                number_of_spaces = 1;
            if(i>1) :
                number_of_spaces = number_of_spaces +2;
            if(i==(line)) :
                number = "*";
        # to PRINT LOWER PYRAMID
        if(line>1) :
            number = " ";
            total_number_of_spaces=2;
            num=line-1;
            number_of_spaces=3+(num*4);
            for i in range (1,line) :
                print(" "*(total_number_of_spaces + i*2) + "-" + " " * (number_of_spaces-4) + "-");
                number_of_spaces=number_of_spaces-4
    print(" "*(4 +(line-1)*2) + "-")
          
k = print_pattern(10.0000);