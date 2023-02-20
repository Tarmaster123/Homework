#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab9_05
def reverse_num(num,result=0):#define reverse_num(num) function to reverse number 
	if num == 0:#base case if num equal to 0 return result(0)
		return result
	else:#combine
		result = result*10 + num % 10#combine by result*10 + num % 10 and keep it in variable result
		return reverse_num(num//10,result)#divide and conquer by num//10 

def main():
	num = int(input("Input Your num : "))
	print(reverse_num(num,result=0))

if __name__ == "__main__":
	main()