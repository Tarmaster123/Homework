#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# HW02_1
# 229223 Sec 002

# define main function 
def main():
    x = float(input(""))#input from user
    area = octagon_area(x)#call octagon_area to find area of octagon
    print("Octagon area: " , area)

#define octagon_area funtion to fine area of octagon
def octagon_area(x):
    octagon_area = 2*(0.5*(x + x/3)*x/3) + (x * x/3)
    return octagon_area

if __name__ == '__main__':
    main()

    
