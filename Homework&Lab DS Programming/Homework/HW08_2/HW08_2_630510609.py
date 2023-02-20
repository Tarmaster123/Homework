#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW08_2
# 229223 Sec 002


def main():
    test_base_b()


def base_b(x, b, result = 0, exp = 0):
    #base case
    if(x == 0):
        return x
    else:
        #Calculte
        result = (x % b) * 10**exp

        #Divide and Conquer
        return result + base_b(x//b, b, result, exp + 1)

def test_base_b():
    assert base_b(8, 2) == 1000
    assert base_b(11, 3) == 102
    assert base_b(55, 4) == 313
    assert base_b(79, 5) == 304
    assert base_b(5872, 6) == 43104
    assert base_b(783, 7) == 2166
    assert base_b(2484, 8) == 4664 
    assert base_b(37192, 9) == 56014 
    assert base_b(18, 10) == 18
    print("All OK!!")               

if __name__ == "__main__":
    main()
