#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab06_5
def longest_digit_run(n):#difine longest_digit_run function
    intersect = 1 #Set variable intersect for count max of  intersect of number
    times = 1 #Set variable times for count intersect of number
    while(n//10)>0:#condition for loop
        num1 = n%10# num1(unit)
        num2 = (n%100)//10 #num2(tens)
        if num1 == num2:#if num1 equal num2 times up 1
            times += 1
        else:#False
            if intersect < times:#if intersect less than times
                intersect = times#keep  variable intersect in variable times
            times = 1# And reset times to 1
        n //= 10#take n divides 10 if out of condition
    
    if intersect < times:#if intersect less than times
    	times = 1 #set times to 1
    	intersect = times #keep  variable intersect in variable times
        
    return intersect#Retuen intersect
def main():
	print(longest_digit_run(11223344777))
if __name__ == '__main__':
	main()


    
        
