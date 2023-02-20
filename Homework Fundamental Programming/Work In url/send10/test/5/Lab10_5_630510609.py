#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab10_5
def three_digits_to_word(n):#define three_digits_to_word function for return digits to word
	#creat unit_list
	unit_list=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	unit_list1=["", "" ,"twenty" ,"thirty", "forty", "fifty" ,"sixty" ,"seventy" ,"eighty" , "ninety" ]
	#condition to change digits to word
	if n == 0:#if n equal to 0
		return "zero"
	elif n > 0 and n < 20 :#if n between 0 and 20
		result = unit_list[n]
		return result
	elif n < 100:#if n between 20 and 100 but not more than 100
		if n % 10 == 0:
			result = unit_list1[n//10] + unit_list[n % 10]
		else:
			result = unit_list1[(n//10)] + "-" + unit_list[n%10] 
		return result
	elif n < 1000:# if n between 100 and 1000 but not more than 1000
		if (n//10) % 10 == 0:
			result = unit_list[n//100] + " hundred " + unit_list1[(n%100)//10] + unit_list[n % 10]
			return result
		else:
			if n % 10 != 0:
				if n % 100 < 20 and n % 100 > 0  :
					result =  unit_list[n//100] + " hundred " + unit_list[n%100]
				else:
					result = unit_list[n//100] + " hundred "  + unit_list1[(n%100)//10] +"-"+ unit_list[n%10]
			else:
				if n % 100 < 20 and n % 100 > 0:
					result =  unit_list[n//100] + " hundred " + unit_list[n%100]
				else:
					result = unit_list[n//100] + " hundred " + unit_list1[(n%100)//10] 
			return result

def num_to_word(num):#define num_to_word function to change number to word
	word = ""#set word for keep value
	#condition for change number to word
	if num == 0:#if num equal to 0
		return "zero"
	while num > 0:
		if num < 1000:#if num less than 1000
			word += three_digits_to_word(num)
			num = 0
		elif num < 1000000:#if num less than 1000000
			word += three_digits_to_word(int(str(num)[:((len(str(num))) - 3)])) + " thousand "
			num = int(str(num)[-3:])
		elif num < 1000000000:#if num less than 1000000000
			word += three_digits_to_word(int(str(num)[:((len(str(num))) - 6)])) + " million "
			num = int(str(num)[-6:])
		else:
			word += three_digits_to_word(int(str(num)[:((len(str(num))) - 9)])) + " billion "
			num = int(str(num)[-9:])
	return word

				
def main():
	num = int(input("Input num: "))
	print(num_to_word(num))

if __name__ == "__main__":
	main()



