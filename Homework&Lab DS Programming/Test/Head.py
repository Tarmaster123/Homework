from math import log10
def dgt_print_h2(n , dgts=None):
    if(dgts is None):
        dgts = int(log10(n))

        if dgts < 0:
            return

        div = 10**dgts
        dgt_print_h2(n%div, dgts - 1)
        print(n//div, end = " ")


def dgt_print_t1(n, dgts=None):
    if(dgts is None):
        dgts = int(log10(n))

    if(dgts < 0):
        return

    div = 10**dgts
    print(n//div, end = " ")
    dgt_print_t1(n%div, dgts - 1)

num = 345
dgt_print_h2(num)    
print("\n--------")
dgt_print_t1(num)   