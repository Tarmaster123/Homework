#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW03_1
# 229223 Sec 002
import math

def main():
    test_fabric_excess()


def fabric_yards(inches) :
    Yard = math.ceil(inches * 1/36) 
    return Yard 

# implement ฟังก์ชันนี้ให้ถูกต้อง
#Define fabric_excess function to calculate fabric excess yards to inches
def fabric_excess(inches):
    Yard = fabric_yards(inches)
    excess = Yard - (inches * 1/36)
    excess = (excess * 36)
    return excess


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_fabric_excess():
    epsilon = 0.001
    assert math.isclose(fabric_excess(1), 35.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(38), 34.0, abs_tol=epsilon)
    
    print("All OK!")


if __name__ == '__main__':
    main()
