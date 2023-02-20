#!/usr/bin/env python3
# เมธาพร เม้ยกำเนิด (เฟรช)
# 631610317
# HW05_2
# 229223 Sec 002

def main():
    test_rotate()

def rotate(num, pos):
    #position is zero
    if (pos == 0): 
        return num

    num = abs(num)
    number = str(num)

    # pos == lenght of number
    if(abs(pos) == len(number)):
        return num

    #position is positive
    if (pos > 0) : 
        if (pos > (len(number))):
           pos = pos  % (len(number))
        a = num % 10**pos
        b = num // 10**pos
        a = str(a)
        b = str(b)
        re = a + b
        return int(re)

    #position is negativve
    else:
        if (abs(pos) > (len(number))):
            pos = abs(pos) % (len(number)) * -1
            if (pos == 0): 
                return num
        x = num % (10**(len(number)-abs(pos)))
        y = num // (10**(len(number)-abs(pos)))
        x = str(x)
        y = str(y)
        rew = x + y
        return int(rew)

def test_rotate():
    # assert rotate(12345, 3) == 34512
    # assert rotate(-12345, -5) == 12345
    assert rotate(12345, 100) == 12345
    # assert rotate(-12345, 5) == 12345
    # assert rotate(12345, 2) == 45123
    # assert rotate(12345, -1) == 23451
    # assert rotate(12345, -3) == 45123
    # assert rotate(12345, -2) == 34512
    # assert rotate(12345, 1) == 51234
    # assert rotate(12345, 0) == 12345
    # assert rotate(12345, -103) == 45123
    # assert rotate(12345, 103) == 34512
    # assert rotate(12345 , 3) == 34512
    # assert rotate(12345 , 2) == 45123
    # assert rotate(12345 , -3) == 45123
    # assert rotate(12345 , 103) == 34512
    # assert rotate(12345 , -103) == 45123
    # assert rotate(12345 , 0) == 12345
    # assert rotate(-12345 , 1) == 51234
    # assert rotate(0 , 1) == 0
    print("ok")

if __name__ =="__main__":
    main()