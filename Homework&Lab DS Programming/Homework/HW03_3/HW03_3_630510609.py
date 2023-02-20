#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW03_3
# 229223 Sec 002

import math
def main():
    test_nearest_odd()


# implement ฟังก์ชันนี้ให้ถูกต้อง
#Define nearest_odd function to calculate odd number thah nearest input by user
def  nearest_odd(x):
    x = math.ceil(x/2)
    x = 2*x - 1
    return x


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd():
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")


if __name__ == '__main__':
    main()