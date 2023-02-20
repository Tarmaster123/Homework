#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab9_01
def gcd(x, y): #define gcd(x , y) function to finethe gcd number
    if y == 0: #base case if y == 0 retunr x
        return x

    else: 
        return gcd(y,x%y)#Divide and conquer and combine 


def main():
	x = int(input("Input 1st number for GCD: "))
	y = int(input("Input 2nd number for GCD: "))
	if x < 0 : #If x is negative
	    ret_gcd = gcd(y,abs(x)%y)
	else: #if x is positive
	    ret_gcd = gcd(y,x%y)

	print("The GCD of %d and %d: %d" %(x, y, ret_gcd))

if __name__ == "__main__":
	main()

