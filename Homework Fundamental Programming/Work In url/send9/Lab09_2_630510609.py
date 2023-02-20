#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab9_02
def n_base_to_10(n,num,exp=0):#define n_base_to_10(n , num) function to dine base 10 in any base
	if num == 0 :# base case if num equal to 0 return num
		return num
	else:
		result = num%10 * n**exp#Keep value num%10 * n**exp in result , exp is power
		return result + n_base_to_10(n,num//10,exp+1)#Divide and conquer in num//10 and combine is result + n_base_to_10(n,num//10,exp+1) 

def main():
	n = int(input("Input base: "))
	num = int(input("Input number: "))
	print(n_base_to_10(n,num,exp=0))
if __name__ == "__main__":
	main()

