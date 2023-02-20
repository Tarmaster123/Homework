import math
def reverse_number(num):
    if num < 10:
        return num


    digit = int(math.log10(num))
    return (((num%10) * 10**digit) + reverse_number(num//10))

def is_palindrome_number(x):
    if x//10 == 0:
        return 1

    if x == reverse_number(x):
        return True

    else:
        return False


n = int(input("Input number n: "))
palindrome = is_palindrome_number(n)
if palindrome == True :
    print("%d is palindrome number" %(n))
else:
    print("%d is not palindrome number" %(n))

'''
row = int(input("Input row:"))
for i in range(row):
    for j in range(row):
        if j + 1  < row and j  < row - (i+1):#1 4 2    2 3 3   3 2 4  4 1 5  5 - 6
            print("*",end=" ")
        else:
            print(i+1,end=" ")
    print()
'''
'''
def recur_print_star2(row, i):
    if row == i:
        return ""

    else:
        pict = "* "*row + "\n"
        return  pict + recur_print_star2(row-1, i)

def main():
    row = int(input("Enter the number of row:"))
    print(recur_print_star2(row, 0))

if __name__ == '__main__':
    main()
'''