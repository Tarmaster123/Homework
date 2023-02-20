#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# HW04_1
# 229223 Sec 002

def main():
    my_min_mid_max(1 , 2 , 3)
    my_min_mid_max(1 , 3 , 2)
    my_min_mid_max(2 , 1 , 3)
    my_min_mid_max(2 , 3 , 1)
    my_min_mid_max(3 , 1 , 2)
    my_min_mid_max(3 , 2 , 1)
    my_min_mid_max(1 , 1 , 1)
    my_min_mid_max(1 , 1 , 2)
    my_min_mid_max(1 , 2 , 1)
    my_min_mid_max(2 , 1 , 1)

#Find min value mid value and c value
def my_min_mid_max(a , b , c):
    min = a
    mid = b
    max = c

    if(min < max):
        if(min < mid):
            if(mid < max):
                pass
            else:
                keep_max = max
                max = mid
                mid = keep_max
        else:
            keep_min = min
            min = mid
            mid = keep_min
    else:
        keep_max0 = max
        max = min
        min = keep_max0

        if(min < mid):
            if(mid < max):
                min = min
                mid = mid
                max = max
            else:
                keep_max1 = max
                max = mid
                mid = keep_max1
        else:
            keep_min = min
            min = mid
            mid = keep_min

    print("min = " ,min)
    print("mid = " ,mid)
    print("max = " ,max ,"\n")

if __name__ == '__main__':
    main()