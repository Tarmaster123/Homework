#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW02_2
# 229223 Sec 002

#Define main funtion 
def main():
    number = int(input(""))#input number from user
    k = int(input(""))#input k from user
    result = kth_digit(number , k)#call funtion kth_digit to find a result
    print(result)

#Define kth_digit to find a result
def kth_digit(number, k):
    k = 10**k
    j = k * 10
    return abs(int(number/k)-int(number/j)*10)

if __name__ == '__main__':
    main()