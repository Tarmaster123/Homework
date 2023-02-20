def is_prime(x):

	for i in range(2,int((x**0.5)+1)):
		if x % i == 0:
			return False
	return (x != 1)

			 
def factor(x):
	i = 2
	while i <= int((x**0.5)+1):
		if x % i == 0:
			print(i,end = " ")
			if i < x:
				print("*",end=" ")
			x //= i				
		else:
			if i == 2:
				i += 1
			else:
				i += 2

			
def factorize(x):
	if is_prime(x) == (x != 1) :
		print("{} is prime ".format(x),end="")

	else:
		print("{} is ".format(x),end="")
		factor(x)
	print()

def main():
	x = int(input("input = "))
	factorize(x)
if __name__ == '__main__':
	main()

