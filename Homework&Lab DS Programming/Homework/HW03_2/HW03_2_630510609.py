#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW03_2
# 229223 Sec 002

import math


def main():
    test_t_area_by_coord()


# implement ฟังก์ชันนี้ให้ถูกต้อง
# Define t_area_by_coord function to calculate Area of Triangle
def t_area_by_coord(x1, y1, x2, y2, x3, y3):
    x12 = (x1 - x2)**2
    y12 = (y1 - y2)**2
    Euclidean_a = (x12 + y12)**0.5

    x23 = (x2 - x3)**2
    y23 = (y2 - y3)**2
    Euclidean_b = (x23 + y23)**0.5

    x13 = (x1 - x3)**2
    y13 = (y1 - y3)**2
    Euclidean_c = (x13 + y13)**0.5

    s = (Euclidean_a + Euclidean_b + Euclidean_c)/2

    Area = (s*(s-Euclidean_a)*(s-Euclidean_b)*(s-Euclidean_c))**0.5
    return Area


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
# สังเกตวิธีการเขียน test case กรณี output เป็นจำนวนจริง
def test_t_area_by_coord():
    eps = 0.001
    assert math.isclose(t_area_by_coord(2, 0, 0, 0, 0, 2), 2.0, abs_tol=eps)
    assert math.isclose(t_area_by_coord(-1, 0, 0, 1, 1, 0), 1.0, abs_tol=eps)

    print("All OK!")


if __name__ == '__main__':
    main()
