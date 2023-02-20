def ones_digit(x):
    return abs(x)%10

def tens_digit(x):
    return ones_digit((abs(x)//10))

def test_tens_digit():
        print("Testing tens_digit... ",end='')
        assert(tens_digit(123) == 2)
        assert(tens_digit(7890) == 9)
        assert(tens_digit(6) == 0)
        assert(tens_digit(-54) == 5)
        assert(tens_digit(-4) == 0)
        print("Passes all tests!")

test_tens_digit()
