#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# HW05_2
# 229223 Sec 002

#Define main function to call test_rotate_num 
def main():
    test_rotate_num()

def position(num , pos):
    num = str(num)
    lenght_of_num = len(num)

    #pos is positive shift right
    if(pos >= 0):
        #Modify pos
        if(abs(pos) > lenght_of_num):
            pos = abs(pos) % lenght_of_num
        pos = pos * -1
        start = len(num)*-1
        num_last = num[pos::]
        num_first = num[start : pos :]

    #pos is negative shift left
    else:
        #Modify pos
        if(abs(pos) > lenght_of_num):
            pos = abs(pos) % lenght_of_num
        else:
            pos = pos * -1  
        num_first = num[0 : pos]
        num_last = num[pos:]
    result = "".join([num_last,num_first])
    return int(result)

#Define rotate function to rotate number follow to condition
def rotate(num , pos):

    if(num < 0):
        num = num * -1
        result = position(num , pos)
    elif(num == 0):
        return 0
    else:
        result = position(num , pos)
    return result

#Define tes_rotate_num for check input and answer
def test_rotate_num():
    assert(rotate(12345 , 3)) == 34512
    assert(rotate(12345 , 2)) == 45123
    assert(rotate(12345 , -3)) == 45123
    assert(rotate(12345 , 103)) == 34512
    assert(rotate(12345 , -103)) == 45123
    assert(rotate(12345 , 0)) == 12345
    assert(rotate(-12345 , 1)) == 51234
    assert(rotate(0 , 1)) == 0
    print("All OK!!")

if __name__ == '__main__':
    main()