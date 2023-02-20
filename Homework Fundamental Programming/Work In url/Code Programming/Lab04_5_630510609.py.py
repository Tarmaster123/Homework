#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab04_5
import math #import math function
def nearest_odd(x):#define function nearest_odd(x)
    x = math.floor(x)#set x to integer by math.floor(x)
    if x%2 == 0 :
        return int(math.ceil(x)+1)
    else :
        return int(math.floor(x))
    # if x mod 2 equal 0 return math.ceil(x) plus 1 and set it to integer else return math.floor(x) in integer 

def main():#define main function
    x = float(input(""))#input x by user
    print(nearest_odd(x))#show answer of function

if __name__=='__main__':
    main()
    
    
