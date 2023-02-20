#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW02_3
# 229223 Sec 002

#Define main funtion
def main():
    number = int(input(""))#input number from user
    k = int(input(""))#input k from user
    value = int(input(""))#input value from user
    result = set_kth_digit(number , k , value)#call set_kth_digit funtion to find a result
    print(result)

#Define kth_digit to find position to set a digit   
def kth_digit(number , k ):
    kth = (abs(number) % 10**(k + 1) - abs(number) % 10**k) // 10**k
    return kth

#Define set_kth_digit funtion to find a result
def set_kth_digit(number , k , value):
    set = kth_digit(number , k)
    keep_set = set * 10**k
    number -= keep_set

    value *= 10**k
    number += value

    return number

if __name__ == '__main__':
    main()

