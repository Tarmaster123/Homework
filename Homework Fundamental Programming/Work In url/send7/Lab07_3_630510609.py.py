#630510609
#กฤตเมฑ ไทยเจริญ
#003
#Lab7_03
def triangle(n):#Define triangle function to creat triangle followto n by use input
	i = 0#Set start i variable in 0
	j = 0#Set start j variable in 0
	
	while(i < n-1):#Loop condition loop untill i more than or equal n-1
		j = 0#Set point to restore j variable in 0
		if i > 0 :#If i more than 0 print "*" 
			print("*",end=(""))
		while(j < (2 * i) -1 ):#Loop condition after if condition loop untill j more than or equal (2 * i) -1 do print "."  and increase j variable
			print(".",end=(""))
			j += 1
		print("*")#If i > 0 print "*" and increase i variable
		i += 1
	i = 0#If out of loop set i is 0 and do next condition
	
	while(i < n):#Loop condition loop untill i more than or equal n print"* " and increase i variable
		print("* ",end=(""))
		i += 1
	
def main():
	triangle(7)
if __name__ == "__main__":
	main()