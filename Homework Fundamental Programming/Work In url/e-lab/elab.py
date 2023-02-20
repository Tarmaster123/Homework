row = int(input("Input row: "))
for i in range(row) :
    for j in range(i+1):
        if i == j or i % 2 == 0 and i != j: 
            print("*",end=" ")
        else:
            print(".",end=" ")
    print("")