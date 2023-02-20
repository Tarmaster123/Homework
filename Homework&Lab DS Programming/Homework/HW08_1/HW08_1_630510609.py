#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW08_1
# 229223 Sec 002

from math import isclose
def main():
    # test_pi()
    pass


def pi(n , result = 0):
    # base case
    if(n == 0):
        return 3 + result
    
    if(n == 1):
        result = result + 4/(2*3*4)
        return pi(n - 1 , result)


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    main()
