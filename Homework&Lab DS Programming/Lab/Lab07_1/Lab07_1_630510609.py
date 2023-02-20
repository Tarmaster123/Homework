#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab07_1
# 229223 Sec 002

def main():
    test_coner_frame()

def corner_frame(n):
    #create range of list
    n = abs(n)

    range_n = list(range(1 , n+1))

    #calculate for create corner frame
    l_n = list(map(lambda x :str(list(range(x , n + 1))) if x == 1 else str((((str(x)) + ' ') * (x-1))) + str(list(range(x , n + 1))), range_n))
    l_n = list(map(lambda x : x.strip('[]') , l_n))
    result = '\n'.join(l_n).replace(',' , '').replace('\'' , '').replace('[' , '')
    return result + '\n'


def test_coner_frame():
    print(corner_frame(15))
if __name__ == "__main__":
    main()