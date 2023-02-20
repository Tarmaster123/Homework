#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab12_3
def prime_factor(n):
	fact = []
	i = 2
	while i <= n**0.5:
		if n % i == 0 and i != 1:
			fact.append(i)
			n //= i
		else:
			if i >= 3:
				i += 2
			else :
				i += 1
	if n != 1:
		fact.append(n)
	return fact

def coprime_factor(a, b):
	A = prime_factor(a)
	B = prime_factor(b)
	co = []
	timesA = len(A)  
	for i in range(timesA):
		if A[0] in B:
			#print("A0 : ",A[0])
			#print("B0 : ",A[0])
			co.append(A[0])
			#print("co : ",co)
			#A.pop(0)
			re = A.pop(0) 
			B.remove(re)
			#print("Re : ",re)
			#print("A : ",A)
			#print("B : ",B)
		else:
			A.pop(0)
			#print("A : ",A)
				
	return sorted(co)

def main():
	a = 1
	b = 1  
	print(prime_factor(a))
	print(prime_factor(b))
	print(coprime_factor(a, b))

if __name__ == "__main__":
	main()




