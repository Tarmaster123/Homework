#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab06_1
def int_power(x, y):#define int_power function
	result = 1#set result of 1
	if y > 0:#if y(power) more than 0
		for i in range(y):#loop in y times
			result *= x#take result multiply x in y times
	elif y == 0:#if y equal 0
		result = 1#return 1
	else:#False
		result = 1.0#set result in float
		for i in range(-y):#loop in y times in minus range
			result /= x #take result divides x in y times
	return result#return result

def main():
	print(int_power(2.3, 3) )
if __name__ == '__name__':
	main()



