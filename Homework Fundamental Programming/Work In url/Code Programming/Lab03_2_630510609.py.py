#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab03_2
def reverse_digits(x):#define function reverse_digits(x)
    num1 = x%10*1000#calculate num1 to thousands
    x    = x//10#calculate x to hundred
    num2 = x%10*100#calculate num2 to hundreds
    x    = x//10#calculate x to ten
    num3 = x%10*10#calculate num3 to tens
    x    = x//10#calculate x to unit
    num4 = x%10#calculate num4 to tens
    return num1+num2+num3+num4#sum num1,2,3,4 

def main():
    x = int(input("Input "))#set x to integer input by user
    numre = reverse_digits(x)#calculate numre(reverse) from function reverse_digits(x)
    print("Output %d" %(numre))#show numre(reverse)

if __name__ == '__main__' :
    main()




