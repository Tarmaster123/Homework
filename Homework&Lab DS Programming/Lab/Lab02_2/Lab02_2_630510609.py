#!/usr/bin/env python3
# กฤตเมธ-ไทยเจริญ-(กีตาร์)
# 630510609
# Lab02_2
# 229223 Sec 002

def main():
    test_reverse_digits()


# implement ฟังก์ชันนี้ให้ถูกต้อง
def reverse_digits(x):

    keep_first_digit = (x % 10)
    first_digit = keep_first_digit * 1000 
    x = (x - keep_first_digit) / 10

    keep_second_digit = (x % 10) 
    second_digit = keep_second_digit * 100
    x = (x - keep_second_digit) / 10

    keep_third_digit = (x % 10) 
    third_digit = keep_third_digit * 10
    x = (x - keep_third_digit) / 10

    fouth_digit = (x % 10) 
    sum_of_digit = first_digit + second_digit + third_digit + fouth_digit
    return sum_of_digit


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_reverse_digits():
    assert reverse_digits(1234) == 4321
    assert reverse_digits(1) == 1000
    print("All OK!")


if __name__ == '__main__':
    main()
