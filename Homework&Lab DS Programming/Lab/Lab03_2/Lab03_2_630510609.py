#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab03_2
# 229223 Sec 002

import math
def main() :
    test_fabric_yards()

#Define fabric_yards function to calculate inches to yards
def fabric_yards(inches) :
    Yard = math.ceil(inches * 1/36) 
    return Yard 

def test_fabric_yards() :
    #assert fabric_yards(1) == 1
    #assert fabric_yards(35) == 1

    assert fabric_yards(36) == 1

    #assert fabric_yards(38) == 2

    assert fabric_yards(72) == 2
    print("Pass!")


if __name__ == '__main__' :
    main()
