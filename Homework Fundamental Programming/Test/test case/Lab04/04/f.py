import math
def round_to_int(x):
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
def main():
    x = float(input("num = "))
    print(round_to_int(x))            

if __name__ == '__main__':
    main()



            
        
