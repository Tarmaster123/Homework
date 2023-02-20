
def find_base(x,b):
	i = 0
	base = 0
	while x > 0:
		r = x%b
		base += r*(10**i)
		x //= b
		i +=1
	return str(base)

def is_palindrome(x, b):# 0 == -1 1 == -2 2 == -3
	base = find_base(x,b)
	if base[len(base)::-1] == base[0::]:
		return True
	else:
		return False
def main():
	print(is_palindrome(35654745 ,6))

if __name__=="__main__":
	main()
