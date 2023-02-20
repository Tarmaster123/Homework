#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab08_2
# 229223 Sec 002

def main():
    assert reverse_digits(1) == 1
    assert reverse_digits(9) == 9
    assert reverse_digits(10) == 1
    assert reverse_digits(65230900) == 903256
    assert reverse_digits(11111) == 11111
    assert reverse_digits(1234) == 4321
    assert reverse_digits(-1234) == -4321
    assert reverse_digits(0) == 0
    assert reverse_digits(12300) == 321
    assert reverse_digits(1001) == 1001
    print("All okKK")

def positive_case(x , result = 0):
    # base case
        if(x == 0):
            return result

        # divide & conq
        else:
            # combine
            result = (result * 10) + (x % 10)
        return positive_case(x//10 , result)

def negative_case(x , result = 0):
     # base case
        if(x == 0):
            return result * -1

        # divide & conq
        else:
            # combine
            x = abs(x)
            result = (result * 10) + (x % 10)
            return negative_case(x//10 , result)
    

def reverse_digits(x):

    if(x >= 0):
        result = positive_case(x, result = 0)
    else:
        result = negative_case(x)
    return result

if __name__ == "__main__":
    main()