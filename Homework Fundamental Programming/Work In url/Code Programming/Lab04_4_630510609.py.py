#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab04_4
import math#import math function
def round_to_int(x):#define function round_to_int(x)
    #if x more or equal 0 do in if bit less than 5 return math.floor(x) else return math.ceil(x) but not
    #do in else if bit less than 5 return math.ceil(x) else return math.floor(x)
    if x >= 0:
        if (x * 10)%10 < 5:
            return math.floor(x)
        else :
            return math.ceil(x)
    else :
        if (abs(x * 10))%10 < 5:
            return math.ceil(x)    
        else :
            return math.floor(x)  
def main():#defeine function main 
    x = float(input("num = "))#input x by user and set it to float
    print(round_to_int(x))  #show answer          

if __name__ == '__main__':
    main()



            
        
