#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab02_3
print("First Equation")
m1 = float(input("Input m1: "))#Set m1 to float
b1 = float(input("Input b1: "))#Set b1 to float
print("Second Equation")
m2 = float(input("Input m2: "))#Set m2 to float
b2 = float(input("Input b2: "))#Set b2 to float
x = float((b2-b1)/(m1-m2))#Calculate variable x for y by (b2-b1)/(m1-m2) and set it to float
y = float(m1*x + b1)#Calculate variable y by take x in equation (b2-b1)/(m1-m2) and set it to float
print("The point of intersection is at x = %.2f and y = %.2f " %(x,y))#Set %.2f in the first to variable x and in the second to variable y  
