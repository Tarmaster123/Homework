#!/usr/bin/env python3
# เมธาพร เม้ยกำเนิด (เฟรช)
# 631610317
# HW10_1
# 229223 sec002

def main():
    test_float_to_base_b()

def float_to_base_b(x, b):
    decimal = x - int(x)
    f = floatconvert(abs(decimal), b)
    int_ = []

    if b <= 10:
        baseb =  str(base_b(int(x), b))
        return baseb + '.' + f
    else:
        if int(x) < 0:
            abx = abs(int(x))
        else:
            abx = x
        if int(abx) == 0:
            return '0' + '.' + f
        while int(abx) != 0:
            r = str(int(abx) % b)
            if r == "10":
                r = "A"
            elif r == "11":
                r = "B"
            elif r == "12":
                r = "C"
            elif r == "13":
                r = "D"
            elif r == "14":
                r = "E"
            elif r == "15":
                r = "F"
            int_.insert(0,r)
            abx = abx // b
        ans = "".join(int_)
        if x < 0: 
            return '-'+ ans + '.'+ f
        return ans + '.' + f

def base_b(x, b):
    base = []
    some = x   
    if x == 0:
        return '0'
    while abs(x) != 0:
        r = str(int(abs(x)) % b)
        base.insert(0,r)
        x = abs(x) // b
    anw = "".join(base)
    if some < 0:
        return '-' + anw
    return anw
    
def floatconvert(j, b):
    float_ = []
    i = 1
    while i <= 6:
        r = int(j*b)
        if r == 10:
            r = "A"
        elif r == 11:
            r = "B"
        elif r == 12:
            r = "C"
        elif r == 13:
            r = "D"
        elif r == 14:
            r = "E"
        elif r == 15:
            r = "F"
        float_.append(str(r))
        j = (j*b)-int(j*b)
        i += 1
    float_ = "".join(float_)
    return float_


def test_float_to_base_b():
    assert float_to_base_b(44.1875, 2) == "101100.001100"
    assert float_to_base_b(0.99999999, 2) == "0.111111"
    assert float_to_base_b(-3.1415, 3) == "-10.010211"
    assert float_to_base_b(0.9375, 16) == "0.F00000"
    assert float_to_base_b(1.0, 2) == "1.000000"
    assert float_to_base_b(-1.0, 2) == "-1.000000"
    assert float_to_base_b(9375.9375, 16) == "249F.F00000"
    assert float_to_base_b(-9375.9375, 16) == "-249F.F00000"
    assert float_to_base_b(44, 2) == "101100.000000"
    assert float_to_base_b(0.0, 2) == "0.000000"
    assert float_to_base_b(1234, 11) == "A22.000000"
    assert float_to_base_b(1234, 13) == "73C.000000"
    assert float_to_base_b(1234, 12) == "86A.000000"
    assert float_to_base_b(1234, 14) == "642.000000"
    assert float_to_base_b(1234, 15) == "574.000000"
    assert float_to_base_b(1234.20, 15) == "574.300000"
    assert float_to_base_b(1000000, 15) == '14B46A.000000'
    print (float_to_base_b(-0.14, 11))
    print (float_to_base_b(-0.0, 11))
    print("ALL OK!!!")
    
if __name__ == '__main__':
    main()