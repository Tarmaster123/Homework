#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab08_1
def square_frame(n,sep=" "):#Define square_frame function to creata square frame
	max_ = (n**2) - ((n - 2) ** 2)#Check max num ber by (n**2) - ((n - 2) ** 2)
	keep_num = []#creatr list keep_num
	for i in range(1,max_+1):#Loop for run number to max
		if i < 10:#if i less thane  10 add 0 infront of i and keep in keep_num
			keep_num.append("0" + str(i))
		else:#else keep it in keep_num
			keep_num.append(str(i))
	#create square frame
	jn = -1
	for j in range(len(keep_num) - 1):#
		if j < n:
			if j == n - 1:
				print(keep_num[j] , end="")
			else:
				print(keep_num[j] , end=sep)
		elif j < n + (n - 2) and n <= j:
			print()
			print(str(keep_num[jn]) + (sep * (n - 1) + ((sep * 2) * (n - 2))) + str(keep_num[j]) , end="")
			jn -= 1
	print()
	#create last line in square frame by start jn stop jn * 2 step -1
	for k in range(jn , (jn * 2 ) - 1 , -1):
		if k == (jn * 2):
			print(keep_num[k])
		else:
			print(keep_num[k] , end=sep)
def main():
	 square_frame(26)


if __name__ == "__main__":
	main() 
	






	