#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab10_2
# 229223 Sec 002

def main():
    test_comma_separated()
    #print(comma_separated(1000000))

    
def comma_separated(n, digit = 3):
    list_n = []
    digit = abs(digit)
    if(digit >= len(str(n))):
        print(n)
    else:
        while(n != 0):
            n = str(n)
            back = n[-digit::1]
            list_n.insert(0, back)
            n = int(n)
            n //= (10**digit)
        result = ",".join(list_n)
        print(result)


def test_comma_separated():
    comma_separated(3400, -3) 
    comma_separated(3400, 4) 
    comma_separated(781588, 5) 
    comma_separated(1234) 
    comma_separated(1000000) 
    comma_separated(10000000,100000000000000000000000000000000000000000000000000000000) 

if __name__ == "__main__":
    main()