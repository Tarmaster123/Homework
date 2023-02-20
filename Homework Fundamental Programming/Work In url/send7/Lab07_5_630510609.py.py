#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab07_5
def rotate(num, pos):#Define rotate funtion to rotate num follow to pos by user input
	i = 0#Set start i variable in 0
	count = 0#Set start count variable in 0
	n = num#Keep num variable in n variable
	if pos == 0:#If condition to check input is 0 
		return num#Resurn num because don't to rotate
	elif pos > 0:#If pos more than 0
		while num > 0:#Loop condition loop untill num lees than oe equal 0 to check count of digit 
			num //= 10
			i += 1
		for c in range(pos):#Loop condition loop pos times 
			n2 = n//10#1Keep value n divide 10 in n2
			n1 = n%10#Kee pn mod 10 value in n1
			result=(n1*10**(i-1))+n2#Calcialte result(count must to rotate) by (n1*10**(i-1))+n2
			n = result#Keep result value in n variable
	else:#iIf not 
		while num > 0:#Loop condition to check count of digit
			num //= 10
			i += 1
		for c in range(abs(pos)):#Loop condition loop absolut pos times
			n2 = n//10**(i-1)#Kee n divide by 10 power i-1 value in n2 variable
			n1 = n%10**(i-1)#Keep n mod by 10 power i-1 in n1 variable
			result=(n1*10)+n2#Calculate result(number count to rotate) by (n1*10)+n2
			n = result#Keep result value in n variable
	return result#Return result 

def main():
	rotate(123456789,0)
if __name__=='__main__':
	main()



