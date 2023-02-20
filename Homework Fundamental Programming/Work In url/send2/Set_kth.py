import kth_digit
def set_kth_digit(number,k,value):
    answer = number - (kth_digit.kth_digit(number,k)*10**k) + (value*10**k) 
    return answer
    
def main():
    number = int(input(""))
    k      = int(input(""))
    value  = int(input(""))
    answer = set_kth_digit(number,k,value)
    print(answer)

if __name__ == '__main__' :
    main()







    
