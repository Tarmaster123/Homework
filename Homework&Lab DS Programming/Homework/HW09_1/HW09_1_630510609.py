#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW09_1
# 229223 Sec 002

def main():
    test_life_path()

def life_path(n):
    #base case
    if(n < 10):
        return n
    else:
        #find sum of number
        n = str(n)
        n_list = list(n)
        total = list(map(lambda x : int(x) , n_list))
        result = sum(total)
        return life_path(result)

def test_life_path():
    assert life_path(13092004) == 1
    assert life_path(7) == 7
    assert life_path(35) == 8
    print("All OK!!")

if __name__ == "__main__":
    main()