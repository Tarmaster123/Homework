#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab04_02
def my_max_mid_min(a,b,c):#define function my_max_mid_min(a,b,c) 
    if a>=b>=c:#if a>=b>=c set max_ = a , mid_ = b , min_ = c and return all value
        max_ = a        
        mid_ = b        
        min_ = c       
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    if a>=c>=b:#but not do if a>=c>=b set max_ = a , mid_ = c , min_ = b and return all value 
        max_ = a
        mid_ = c
        min_ = b
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))   
    if b>=c>=a:#if b>=c>=a set max_ = b , mid_ = c , min_ = a and return all value
        max_ = b
        mid_ = c
        min_ = a
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    if b>=a>=c:#but not do if b>=a>=c set max_ = b , mid_ = a , min_ = c and return all value
        max_ = b
        mid_ = a
        min_ = c
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))    
    if c>=b>=a:#if c>=b>=a set max_ = c , mid_ = b , min_ = a and return all value
        max_ = c
        mid_ = b
        min_ = a
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))
    if c>=a>=b:#but not do if c>=a>=b set max_ = c , mid_ = a , min_ = b and return all value
        max_ = c
        mid_ = a
        min_ = b
        return print("max = %d \nmid = %d \nmin = %d " %(max_,mid_,min_))

def main():#def function main 
    a = int(input(""))#input value a by user
    b = int(input(""))#input value b by user
    c = int(input(""))#input value c by user
    my_max_mid_min(a,b,c)#call function my_max_mid_min(a,b,c)
    return 0#end function

if __name__ == '__main__':
    main()



           












    

