#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab03_5
import Lab03_4#import funtion kth_digit
def set_kth_digit(number,k,value):#define function set_kth_digit(number,k,value)
    answer = number - (Lab03_4.kth_digit(number,k)*10**k) + (value*10**k)#calculate answer from number - (kth_digit.kth_digit(number,k)*10**k) + (value*10**k)
    return answer#restore answer
    
def main():#definr function main()
    number = int(input(""))#set number to integer and input by user
    k      = int(input(""))#set k to integer and input by user
    value  = int(input(""))#set value to integer and input by user
    answer = set_kth_digit(number,k,value)#calculate answer from function set_kth_digit(number,k,value)
    print(answer)#show answer

if __name__ == '__main__' :
    main()







    
