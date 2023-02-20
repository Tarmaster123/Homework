#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW10_2
# 229223 Sec 002

def main():
    test_eratosthenes()

def eratosthenes(n, show_step=False):
    # mark = []
    # p = 2
    # while p < int(n**0.5) + 1:
    #     if p in mark:
    #         p += 2
    #         continue
    #     mark_list = list(filter(lambda x : x % p == 0 and x != p, table_n[table_n.index(p*p):]))
    #     mark.extend(mark_list)
    #     table_n = list(filter(lambda x : x not in mark_list , table_n))
    #     if(show_step == True):
    #         print("%d: "%(p) ,end="")
    #         print(table_n)
    #     if(p + 1 in table_n):
    #         p += 1
    #     else:
    #         p += 2
    # return table_n

    table_n = list(range(2, n + 1))
    p = 2
    while p < int(n**0.5) + 1:
        if p not in table_n:
            p += 2
            continue
        mark_list = list(filter(lambda x : x % p != 0 or x == p, table_n))
        table_n = mark_list
        if(show_step == True):
            print("%d: "%(p) ,end="")
            print(table_n)
        if(p + 1 in table_n):
            p += 1
        else:
            p += 2
    return table_n


    

    

def test_eratosthenes():
    result = eratosthenes(2, True)
    print('----')
    print(result)

    # print()

    # result = eratosthenes(20)
    # print('----')
    # print(result)
    
if __name__ == "__main__":
    main()