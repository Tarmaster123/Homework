import math
def nearest_odd(x):
    x = math.floor(x)
    if x%2 == 0 :
        return int(math.ceil(x)+1)
    else :
        return int(math.floor(x))

def main():
    x = float(input(""))
    print(nearest_odd(x))

if __name__=='__main__':
    main()
    
    
