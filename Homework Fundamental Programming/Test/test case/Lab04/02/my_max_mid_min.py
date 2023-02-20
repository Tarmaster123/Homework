def my_max_mid_min(a,b,c):
    if a>=b>=c:
        max_ = a        
        mid_ = b        
        min_ = c       
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    elif a>=c>=b:
        max_ = a
        mid_ = c
        min_ = b
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))   
    if b>=c>=a:
        max_ = b
        mid_ = c
        min_ = a
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    elif b>=a>=c:
        max_ = b
        mid_ = a
        min_ = c
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))    
    if c>=b>=a:
        max_ = c
        mid_ = b
        min_ = a
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    elif c>=a>=b:
        max_ = c
        mid_ = a
        min_ = b
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))

def main():
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    my_max_mid_min(a,b,c)
    return 0

if __name__ == '__main__':
    main()



           












    

