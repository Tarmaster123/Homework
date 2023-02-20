def factorize(x):
    print(x, "is", end=" ")
    x_init = x
    i = 2
    while i <= (x**0.5):
        if x%i == 0:
            print(i,"*",end=" ")
            x//=i
        else:
            i += 1
    if x == x_init and x_init != 1:
        print("prime")
    else:
        print(x)

def main():
    x = int(input())
    factorize(x)

if __name__ == '__main__':
    main()
