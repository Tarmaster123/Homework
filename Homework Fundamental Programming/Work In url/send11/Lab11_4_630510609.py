#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab11_2
def sum_nested_list(list_a):#Define sum_nested_list for fine sum of number in nested list
	keep_list = []#Create list keep_list
	keep_num = []#Create list keep_num
	keep_sum = []#Create list keep_sum
	for i in list_a:#check each parameters in list_a 
		if isinstance(i , list):#If parameter is list keep it in keep_list(extend)
			keep_list.extend(i)
		else:#else keep it in keep_num(append)
			keep_num.append(i)
	for j in keep_list:#check parameter in keep_list
		if isinstance(j , list):#If it is list keep it in keep_list(extend)
			keep_list.extend(j)
	for k in keep_list:#check parameter in keep_list
		if isinstance(k , int):#If it is integer keep it in keep_num(append)
			keep_num.append(k)
	keep_sum = sum(keep_num)#sum keep_num and keep it in keep_sum
	return keep_sum	#return keep_sum

def main():
	list_a = [81, [[31, [159]], 9577, [22, [181, [41]]]]]
	print(sum_nested_list(list_a))
if __name__ == "__main__":
	main()