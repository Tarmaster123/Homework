def ones_digit(x):
    return abs(x)%10

def Test_ones_digit():
    print("Testing_ones_digit...",end="")
    assert(ones_digit(123) == 3)
    assert(ones_digit(7890) == 0)
    assert(ones_digit(6) == 6)
    assert(ones_digit(-54) == 4)
    assert(ones_digit(-4) == 4)
    print("Passes all tests!")

Test_ones_digit()
