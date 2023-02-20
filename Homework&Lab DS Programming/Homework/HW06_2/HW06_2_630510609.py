#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW06_2
# 229223 Sec 002

#Define main function
def main():
    dest_rotate_list([1, 2, 3, 4] , 4)

def modify_n(list_a , n):
    lenght_of_list_a = len(list_a)

    if(n > 0):
        n = n % lenght_of_list_a
    else:
        n = (abs(n) % lenght_of_list_a) * -1
    return n

#Define dest_rotate_list function
def dest_rotate_list(list_a , n):
    lenght_of_list_a = len(list_a)

    # n is zero or n equal to lenght_of_list_a
    if(n == 0 or abs(n) == lenght_of_list_a or lenght_of_list_a == 1):
        list_a = list_a

    # n is positive
    elif(n > 0):
        if(n > lenght_of_list_a):
            n = modify_n(list_a , n)
        old_lenght = len(list_a)
        n *= -1
        old_list = list_a[old_lenght * -1 : n ]

        list_a.extend(old_list)
        new_lenght = len(list_a)
        del list_a[new_lenght * -1 : old_lenght * -1]

    #n is negative
    else:
        if(abs(n) > lenght_of_list_a):
            n = modify_n(list_a , n)
        modify_n(list_a , n)
        old_lenght = len(list_a)
        old_list = list_a[old_lenght * -1 : (old_lenght + n) * -1 ]

        list_a.extend(old_list)
        new_lenght = len(list_a)
        del list_a[new_lenght * -1 : old_lenght * -1]


if __name__ == "__main__":
    main()