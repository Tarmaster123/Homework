#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab10_3
def nondest_rotate_list(list_a, n):#define nondest_rotate_list to rotate number in list (Non-destructive)
	if n >= 0:#if num is positives 
		for item in range(n):#loop follow by n times
			last = list_a.pop(-1)#cut in last position in list and keep it in last variable
			list_a.insert(0,last)#insert last position in the first position 
	else:#if num is negatives 
		for item in range(abs(n)):#loop follow by absolute n times
			first = list_a.pop(0)#cut in first position in list and keep it in first variable
			list_a.append(first)#add first value back in to list_a
	return list_a#return list_a
def main():
	list_a = [1, 2, 3, 4]
	n = int(input(""))
	print(nondest_rotate_list(list_a, n))
if __name__ =="__main__":
	main()
