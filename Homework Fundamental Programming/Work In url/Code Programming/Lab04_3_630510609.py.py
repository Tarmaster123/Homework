#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab04_3
def calculate_p2p_evolve_exp(p,c): #Define calculate_p2p_evolve_exp function.
    nc = 11*p+1 #Calculate nc by 11*p+1
    print(nc)
    if c > nc: #If c more than nc
            c = nc #Set c equal nc
            exp = ((c + (p-1)) //12) * 500 #Calculate exp by ((c + (p-1)) //12) * 500
            return exp #Retuen exp
    else: #But not.
        if c==0 and p==0: #If c and p equal 0
            return 0 #Return 0
        else: #But not 
            exp = ((c + (p-1)) //12) * 500 #Calculate exp by ((c + (p-1)) //12) * 500
            return exp #Return exp
def main():
    p = int(input(""))
    c = int(input(""))
    exp = calculate_p2p_evolve_exp(p,c)
    print(exp)

if __name__ == '__main__':
    main()
