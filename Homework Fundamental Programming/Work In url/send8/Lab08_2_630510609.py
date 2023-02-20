#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab8_02
def find_base(x,b):#define function find base to change x in any base
	i = 0
	base = 0
	while x > 0:
		r = x%b
		base += r*(10**i)
		x //= b
		i +=1
	return str(base)

def is_palindrome(x, b):#define function to check parindeome number
	base = find_base(x,b)#take value by find_base(x,b) and keep it in base variable
	if base[len(base)::-1] == base[0::]:#if reverse base equal to base(original) return True
		return True
	else:#If not
		return False#return False
def main():
	print(is_palindrome(7043,6))
	
if __name__=="__main__":
	main()
