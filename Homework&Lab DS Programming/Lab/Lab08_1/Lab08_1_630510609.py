#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab08_1
# 229223 Sec 002

def main():
    assert(gcd(19 , 71) == 1)
    assert(gcd(-39 , 78) == 39)
    print("All OK!!")
def gcd(x,y):
    x = abs(x)
    y = abs(y)

    # base case
    if(x % y == 0):
        return y
    return gcd(y , x % y)

if __name__ == "__main__":
    main()

