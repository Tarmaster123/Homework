#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab7_02
import math#Import math function
def digit_count(x, base=10):#Define digit_count fuction to count digit each of base
	n = base#Keep variable base in n variable   
	result = math.ceil(math.log(abs(x)+1,n))#Calculate result by math.ceil(math.log(abs(x)+1,n))
	return result#Return result 
def main():
	assert(digit_count(258) == 3)#If user input x variable and don't input base variable in to digit_count number.This function takes absolut x plus 1 and calculate base 10 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 2) == 9)##If user input x variableand input base variable in 2 to digit_count number.This function takes absolut x plus 1 and calculate base 2 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 3) == 6)##If user input x variableand input base variable in 3 to digit_count number.This function takes absolut x plus 1 and calculate base 3 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 4) == 5)##If user input x variable and nput base variable in 4 to digit_count number.This function takes absolut x plus 1 and calculate base 4 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 5) == 4)##If user input x variableand input base variable in 5 to digit_count number.This function takes absolut x plus 1 and calculate base 5 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 6) == 4)##If user input x variableand input base variable in 6 to digit_count number.This function takes absolut x plus 1 and calculate base 6 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 7) == 3)##If user input x variableand input base variable in 7 to digit_count number.This function takes absolut x plus 1 and calculate base 7 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 8) == 3)##If user input x variableand input base variable in 8 to digit_count number.This function takes absolut x plus 1 and calculate base 8 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 9) == 3)##If user input x variableand input base variable in 9 to digit_count number.This function takes absolut x plus 1 and calculate base 9 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 11) == 3)##If user input x variableand input base variable in 11 to digit_count number.This function takes absolut x plus 1 and calculate base 11 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 12) == 3)##If user input x variableand input base variable in 12 to digit_count number.This function takes absolut x plus 1 and calculate base 12 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 13) == 3)##If user input x variableand input base variable in 13 to digit_count number.This function takes absolut x plus 1 and calculate base 13 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 14) == 3)##If user input x variableand input base variable in 14 to digit_count number.This function takes absolut x plus 1 and calculate base 14 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 15) == 3)##If user input x variableand input base variable in 15 to digit_count number.This function takes absolut x plus 1 and calculate base 15 of absolute x by math.log function and round this number by use math.ceil function. 
	assert(digit_count(258, 16) == 3)##If user input x variableand input base variable in 16 to digit_count number.This function takes absolut x plus 1 and calculate base 16 of absolute x by math.log function and round this number by use math.ceil function. 

if __name__ == "__main__":
	main()
'''def test_digit_count():
	print(digit_count(-177147))
	assert(digit_count(-177147,3) == 12)
	assert(digit_count(258 , 2) == 9)
test_digit_count()'''


	


