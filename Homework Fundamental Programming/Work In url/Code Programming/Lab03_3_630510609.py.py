#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab03_3
def octagon_area(x):#define function octagon_area(x)
    area = 2*((1/2)*(x+(x/3))*(x/3))+(x*(x/3))#calculate area from 2*((1/2)*(x+(x/3))*(x/3))+(x*(x/3))
    return area#restore area

def main():#define function main
    x = float(input("Input x: "))#set x to float and input by user
    Area = octagon_area(x)#calculate Area from function octagon_area(x)
    print("Area is %f" %Area)#show Area 
    
if __name__ == '__main__' :
    main()

    
    
