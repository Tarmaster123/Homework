#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab04_2
# 229223 Sec 002

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function is_p_triple()

def main():
    test_p_triple()


def is_p_triple(x, y, z):
    #Check if some parameter isn't integer return False
    if(type(x or y or z) != int ):
        return False
    #Check x
    if(x == (y**2 + z**2)**0.5):
        return True
    #Check y
    if(y == (x**2 + z**2)**0.5):
        return True
    #Check z
    if(z == (x**2 + y**2)**0.5):
        return True
    return False

def test_p_triple():
    assert is_p_triple(4, 5, 3) == True
    assert is_p_triple(42, 9, 41) == False
    print("all ok!")


if __name__ == '__main__':
    main()