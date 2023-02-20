#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW09_2
# 229223 Sec 002

def main():
    test_longest_digit_run()
    #print(longest_digit_run(11777332))

def longest_digit_run(n , keep = 1, max_ = 0):
    #base case
    if(n == 0):
        return max_
    else:
        #negative case
        n = abs(n)

        #find max digit
        if(n % 10 == (n//10)%10):
            keep += 1
            return longest_digit_run(n//10 ,keep, max_)
        else:
            if(keep >= max_):
                max_ = keep
                keep = 1
                return longest_digit_run(n//10 , keep, max_)
            else:
                keep = 1
                return longest_digit_run(n//10 , keep, max_)


def test_longest_digit_run():
    assert longest_digit_run(11777332) == 3
    assert longest_digit_run(1177332) == 2
    assert longest_digit_run(1234567) == 1
    assert longest_digit_run(22) == 2
    assert longest_digit_run(2) == 1
    assert longest_digit_run(0) == 0
    assert longest_digit_run(-11777332) == 3
    print("All OK!!!!")

if __name__ == "__main__":
    main()