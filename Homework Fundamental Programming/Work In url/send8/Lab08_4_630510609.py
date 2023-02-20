#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab8_04
def uniform(line):#define uniform(line) to change character input by user in all upper or lower 
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#Creat all upper charactor
	lower = "abcdefghijklmnopqrstuvwxyz"#Creat all lower charactor
	countup = 0#Set start conuntup(upper) is 0
	countdown = 0#Set start conuntdown(lower) is 0
	for i in line:#loop condition
		if i in upper:#if loop i in upper then have increase countup
			countup += 1
		elif i in lower:#if loop i in lower then have increase countdown
			countdown += 1

	if countup == countdown:#if countup equal countdown
		if line[0] in upper:#Check first charactor if have in upper return line upper
			return line.upper()			
		else:#if not return line lower
			return line.lower()
			
	elif countup > countdown:#if countup more than count down return line upper
		return line.upper()			
	else:#if not
		return line.lower()#return line lower

		

def main():
	line = input("")
	print(uniform(line))
if __name__=="__main__":
	main()


	




