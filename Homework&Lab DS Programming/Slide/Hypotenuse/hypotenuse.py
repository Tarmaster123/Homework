#!/usr/bin/env python3

def hypotenuse(a,b):
    h = ((a**2) + (b**2)) ** 0.5
    return h

def main():
    s1 = float(input("input a: "))
    s2 = float(input("input b: "))
    h = hypotenuse(s1 , s2)

    print("hypotenuse = {0:.2f}" . format(h))

if __name__ == '__main__':
    main()