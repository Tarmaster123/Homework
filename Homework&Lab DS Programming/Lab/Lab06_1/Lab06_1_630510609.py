#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab06_1
# 229223 Sec 002


def main():
    test_triangle()

#create triangle pattern follow n from user
def triangle(n):
    n = abs(n)
    if(n < 3):
        return "\n"
    range_ = list(range(1 , n+1))
    star_list = list(map(lambda x : '* ' * x  if x == 1 or x == n else '*' + ('.' * ((2*(x-1)) - 1)) + '*'  , range_))
    result = '\n'.join(star_list)
    return str(result) + '\n'


def test_triangle():

    T3 = '''
*
*.*
* * *

'''

    T7 = '''
*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *

'''
    print(triangle(4))
    # assert triangle(3) == T3
    # assert triangle(7) == T7
    # print("OK")


if __name__ == '__main__':
    main()
