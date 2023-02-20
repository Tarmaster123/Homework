#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab06_2
def float_to_bin(x):#difine float_to_bin function to fine binary number
	init_x = x#Set init_x for keep variable x is stable
	result_int = 0#Set start value result_int
	i = 0#Set start value i
	int_ = True #True is value is plus
	decimalx = decimal(abs(x))#Keep decimal(abs(x)) in variable decimalx
	if x == 0:#If x equal 0 retuurn it to 0.000000
		return 0.000000
	elif x < 0:#If x less than 0 so value is minus and set x to absolute x to set it to plus
		int_ = False
		x = abs(x)
	while x > 0:#condition loop if x more than 0 loop it
		r = x%2#r mod 2 for take fraction
		result_int += r*(10**i)# Cal result by result_int = result + r*(10**i)
		x //= 2#take x divide 2
		i += 1#Up i 1
	if int_ == True:#If int_ is True value is plus
		Binary = int(result_int) + decimalx #Cal Binary by int(result_int) + decimalx
	else:#If not
		Binary = (int(result_int) + decimalx) * (-1)#Cal Binary by int(result_int) + decimalx and multiply -1
	return float("%.6f"%(Binary))#Return Binary to float

def decimal(x):#Difine decimal function to find decimal
	result_deci1 = x%1#Keep x mod 1 in result_deci1 variable
	result_deci2 = 0#Set start value result_deci2 is 0
	i = -1 #Set i to -1
	while result_deci1 < 1 :#condition loop if result_deci1 less than 1 loop it
		r1 = result_deci1 * 2#Keep result_deci1 * 2 in r1
		result_deci2 += r1//1*(10**i)#Cal decimal in binary by result_deci2 = result_deci2+r1//1*(10**i)
		result_deci1 = r1%1#Keep value r1 in result_deci1
		if result_deci1 == 0 or abs(i)-1 == 6:#if result_deci1 equal 0 or abs(i)-1 == 6 out  of loop
			break
		i -= 1
	return result_deci2#Return esult_deci2

def main():
	print(float_to_bin(289) )
	print("Pass")

#if __name__ == '__name__':
main()


