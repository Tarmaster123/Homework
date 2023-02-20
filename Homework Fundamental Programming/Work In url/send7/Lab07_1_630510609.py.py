#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab7_01
def is_prime(x,y):#Define is_primt function to check prime number
	for i in range(2,y+1):
		if x % i == 0 and i != x: 
			return False
	return True

def sum_prime_in_range(x, y):#Define sum_prime_in_range to calculate sum of prime
	sum_prime = 0#Set start value of sum_prime is 0
	j = 2#Set start value of j is 2
	for j in range (x,y+1):#Loop condition to set count to calculate
		if is_prime(j,y):#If j is prime take  sum_prime plus j  
			sum_prime += j
	return sum_prime#Return sum of prime 
def main():
	x = int(input(""))
	y = int(input(""))
	print(sum_prime_in_range(x, y))
if __name__=='__main__':
	main()




