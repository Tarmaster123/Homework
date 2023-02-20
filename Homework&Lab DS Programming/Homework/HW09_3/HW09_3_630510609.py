#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW09_3
# 229223 Sec 002

def main():
    test_left_max()

def left_max(n, index = 0):
    #base case
    if(index+1 == len(n)):
        return n
    else:
        #copy list
        new_list = n[:]

        #change value in new_list
        if(new_list[index+1] >= new_list[index]):
            new_list[index+1] = new_list[index+1]
        else:
            new_list[index+1] = new_list[index]
        return left_max(new_list, index+1)

def test_left_max():
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    print("All OK!!!")

if __name__ == "__main__":
    main()