from math import sqrt

def is_standard(w,h):
    return h/w <= sqrt(2)+0.001 and h/w >= sqrt(2)- 0.001

def test_is_standard():
    assert(is_standard(841,1189)==True) # A0
    assert(is_standard(594,841)==False) # A1
    assert(is_standard(420,594)==True) # A2
    assert(is_standard(297,420)==True) # A3
    print("Pass all tests!")

test_is_standard()
