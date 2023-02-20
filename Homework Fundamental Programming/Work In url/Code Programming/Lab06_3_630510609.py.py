def is_prime(x):

	for i in range(2,int((x**0.5)+1)):
		if x % i == 0:
			return False
	return True

			 
def factor(x):
	i = 2
	while i <= (x**0.5): 
		if x % i == 0 and is_prime(i):
			print(i,end = " * ")
			x /= i				
		else:
			i += 1
	print(int(x))
			
def factorize(x):
	if is_prime(x) == True :
		print("%d is prime"%(x))

	else:
		print("%d is"%(x),end=" ")
		factor(x)

def main():
	x = int(input("input = "))
	factorize(x)
if __name__ == '__main__':
	main()

