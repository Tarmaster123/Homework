#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab9_03
def is_prime(n , i = 2):#define is_prime(n) function to check prime number and set parameter i is 2
	if n == 1 : #first base case is n equal 1 so it is't prime number return False 
		return False
	if i + 1 == n:#combine if sum of i and 1 is equal to n so it is prime number and return True
		return True
	if n == 2 :#second base case is n equal 2 so it is prime number return it to True 
		return True
	if  n % i == 0:#combine if  n mod i equal to 0 so it is't prime number return it to False 
		return False
	else:
		return is_prime(n , i + 1)#divide and conquer by increase i 

def main():
	n = int(input("Input your number: "))
	print(is_prime(n, i=2))

if __name__ =="__main__":
	main()
