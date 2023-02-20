def octagon_area(x):
    area = 2*((1/2)*(x+(x/3))*(x/3))+(x*(x/3))
    return area

def main():
    x = float(input("Input x: "))
    Area = octagon_area(x)
    print("Area is %f" %Area)
    
if __name__ == '__main__' :
    main()

    
    
