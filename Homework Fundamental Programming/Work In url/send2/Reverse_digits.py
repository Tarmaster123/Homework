def reverse_digits(x):
    num1 = x%10*1000
    x    = x//10
    num2 = x%10*100
    x    = x//10
    num3 = x%10*10
    x    = x//10
    num4 = x%10
    return num1+num2+num3+num4

def main():
    x = int(input("Input "))
    numre = reverse_digits(x)
    print("Output %d" %(numre))

if __name__ == '__main__' :
    main()




