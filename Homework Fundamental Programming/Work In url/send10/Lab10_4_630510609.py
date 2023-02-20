#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab10_4
def dest_rotate_list(list_a, n):#define nondest_rotate_list to rotate number in list (Destructive)
	if n >= 0:#if num is positives
		for item in range(n):#loop follow by n times
			last = list_a.pop(-1)#cut in last position in list and keep it in last variable
			result = list_a.insert(0,last)#insert last position in the first position and keep it in result vaariable
	else:#if num is negatives 
		for item in range(abs(n)):#loop follow by absolute n times
			first = list_a.pop(0)#cut in first position in list and keep it in first variable
			result = list_a.append(first)#add first value back in to list_a


def main():
	list_a = [1, 2, 3, 4]
	n = int(input(""))
	print(dest_rotate_list(list_a, n))
	print(list_a)

if __name__ =="__main__":
	main()

