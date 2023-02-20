#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab10_1
# 229223 Sec 002

def main():
    test_bean_count()

def bean_count(n):
    bean = 0
    if(n <= 0) or (n % 100 == 0):
        bean = 0
        return bean

    while n != 0:
        n %= 100
        for i in range(1, n+1):
            if(i % 100 == 0):
                bean = 0
            elif(i % 10 == 0):
                bean -= 5
            else:
                bean += 1
        n //= 100
    return bean



def test_bean_count():
    assert bean_count(-10) == 0
    assert bean_count(90) == 36
    assert bean_count(202) == 2
    assert bean_count(212) == 6
    assert(bean_count(11111111)) == 5
    print("All OK!!!!")

if __name__ == "__main__":
    main()