#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab03_1
# 229223 Sec 002

import math
def main() :
    test_fibonacci_number()


def nth_fibonacci_number(n) :
    Fi = (1 + 5**0.5)/2
    Answer = math.floor((Fi**n / 5**0.5) + 0.5)
    return Answer


def test_fibonacci_number() :
    assert nth_fibonacci_number(3) == 2
    assert nth_fibonacci_number(8) == 21
    print("Pass!!")


if __name__ == '__main__' :
    main()
