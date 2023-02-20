#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab07_4
def life_path(n):#Deffine life_path to calculate sum of each digit of number 
	result = 0#Set star result variable is 0 
	result_2 = 0#Set star result_2 variable is 0 
	result_3 = 0#Set star result_3 variable is 0 
	while n > 0:#Loop condition loop untill n less than or equal 0
		n1 = n%10#Keep n variable mod 10 value in n1 variable
		result += n1#Take n1 variavble increase to result
		n //= 10#Take n variable divide by 10 
	result_1 = result#Keep result variable in result_1

	while result_1 > 0:#Loop condition loop untill result_1 more than or equal 0
		n2 = result_1%10#Keep result_1 mod 10 value in n2 variable
		result_2 += n2#Take n2 variavble increase to result_2
		result_1 //= 10#Take result_1 divides by 10

	while result_2 > 0:#Loop condition loop untill result_2 more than or equal 0
		if result_2 == 10:#If result equal 10 return value 1
			return 1
		else:#If not
			n3 = result_2%10#Keep result_2 mod by 10 value in n3 variable
			result_3 += n3#Take n3 increase to result_3
			result_2 //= 10#Take result_2 divides 10
	return result_3 #Retuen result_3

def main():
	assert(life_path(13011994) == 1)
	assert(life_path(7) == 7)
	assert(life_path(32) == 5)
	print("Pass all")
	
if __name__=='__main__':
	main()
	
