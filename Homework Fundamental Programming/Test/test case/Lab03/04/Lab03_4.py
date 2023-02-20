def kth_digit(number,k):
    return number//10**(abs(k))%10

def main():
    number = int(input(""))
    k   =    int(input(""))
    answer = kth_digits(number,k)
    print(answer)

if __name__ == '__main__' :
    
    main()

