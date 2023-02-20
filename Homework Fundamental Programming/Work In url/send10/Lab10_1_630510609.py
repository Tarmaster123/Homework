#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab10_1
import string #import string 
def is_anagram(str1, str2):#define is_anagram for check character anagram 
	remove1 = string.whitespace#remove white space
	remove2 = string.punctuation#remove punction
	remove3 = string.digits#remove digits
	lo1 = str1.lower()#change str1 to lower and keep it in lo1 variable
	lo2 = str2.lower()#change str2 to lower and keep it in lo1 variable
	List1 = list(lo1)#change lo1 to list and keep it in List1 variable
	List2 = list(lo2)#change lo2 to list and keep it in List2 variable
	series1 = sorted(List1)#sort List1 and keep it in series1 variable
	series2 = sorted(List2)#sort List2 and keep it in series2 variable
	result1 = list(filter(lambda x: x not in remove1+remove2+remove3 , series1))#remove white punction and digits in series1
	result2 = list(filter(lambda x: x not in remove1+remove2+remove3 , series2))#remove white punction and digits in series2
	if result1 == result2:#Compare result1 and result2 if equal return True else return False
		return True
	else:
		return False

def main():
	str1 = input("Input 1: ")
	str2 = input("Input 2: ")
	print(is_anagram(str1, str2))
if __name__ == "__main__":
	main()


