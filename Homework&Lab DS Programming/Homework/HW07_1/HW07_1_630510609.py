#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW07_1
# 229223 Sec 002


def main():
    square_frame(26 , " ")
    

def square_frame(n, sep=' '):
    #find max of square and create list
    n = abs(n)
    max_of_square = n**2 - (n - 2)**2
    range_of_middle = list(range(1 , n-1 ))
    list_n = list(range(1 , max_of_square + 1))

    # add zero frint number
    add_zero = list(map(lambda x : ('0' * (len(str(list_n[-1]))- len(str(x))))+str(x) , list_n))

    # first line
    first_line = str(list(add_zero[:n]))


    #last line
    max_of_lastline = (max_of_square - (n - 2)) - 1
    min_of_lastline = (n + (n - 1)) - 2
    last_line = str(list(add_zero[max_of_lastline : min_of_lastline : -1]))


    if(sep == ' '):
        first_line = first_line.strip('[]').replace(',' , '').replace('\'' , '')
        last_line = last_line.strip('[]').replace(',' , '').replace('\'' , '')
    else:
        if(sep == '\''):
            first_line = first_line.strip('[]').replace('\'' , '').replace(',' , sep).replace(' ' , '')
            last_line = last_line.strip('[]').replace('\'' , '').replace(',' , sep).replace(' ' , '')
        else:
            first_line = first_line.strip('[]').replace(',' , sep).replace('\'' , '').replace(' ' , '')
            last_line = last_line.strip('[]').replace(',' , sep).replace('\'' , '').replace(' ' , '')

    # midle line
    middle_line =  list(map((lambda x : add_zero[x * -1] + sep*(n) + add_zero[(n - 1 ) + x] if n == 3 else add_zero[x * -1] + sep * ((len(first_line) - (len(add_zero[-1]) * 2))) + add_zero[(n - 1 ) + x] ) , range_of_middle))      
    middle_line = '\n'.join(middle_line)

    print(first_line)
    print(middle_line)
    print(last_line)

if __name__ == "__main__":
    main()