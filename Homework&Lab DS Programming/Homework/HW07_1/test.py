#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW07_1
# 229223 Sec 002


def main():
    square_frame(26)
    


def zero_padding(n , x):
    max_of_n = n**2 - (n - 2)**2
    range_of_max_n = list(range(1 , max_of_n + 1))
    len_max_str = len(str(range_of_max_n[-1]))
    len_str = len(str(x))
    if(len_str < len_max_str):
        return ('0'*(len_max_str - len_str)) + str(x)
    else:
        return str(x)

def square_frame(n, sep=' '):
    # max of range
    max_of_n = n**2 - (n - 2)**2
    range_of_max_n = list(range(1 , max_of_n + 1))
    range_of_n = list(range(1 , n - 2))

    # zero padding
    zero_pad = list(map(lambda x : zero_padding(n , x) , range_of_max_n))
    
    # first line 
    first_line = str(list(zero_pad[:n]))

    # last line 
    max_of_lastline = (max_of_n - (n - 2)) - 1
    min_of_lastline = (n + (n - 1)) - 2
    last_line = str(list(zero_pad[max_of_lastline : min_of_lastline : -1]))

    # middle line
    middle_line = list(map(lambda x : zero_pad[x * -1] + sep * ((len(first_line) - (len(zero_pad[-1]) * 2))) + zero_pad[(n - 1 ) + x] , range_of_n))

    middle_line = '\n'.join(middle_line)
    
    print(first_line)
    print(middle_line)
    print(last_line)

    
if __name__ == "__main__":
    main()