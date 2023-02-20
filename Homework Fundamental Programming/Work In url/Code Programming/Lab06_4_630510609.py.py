#630510609
#กฤตเมธ ไทยยเจริญ
#003
#Lab06_4
def Cal_score():#define Cal_score funtion to find max score runner and average score
	#Set start value in 0
	num1 = 0
	num2 = 0
	first = 0
	second = 0
	average = 0
	n_s = int(input("Total students: "))#input number of student from user
	print("Enter score:")#Show text Enter score 
	for i in range(1,n_s+1):#Condition loop in range 1 to number of studen
		score1 = first#Keep variable first in score1 
		score2 = second#Keep variable second in score2 
		num = int(input())#input value num by user 
		if num > score1:#if num more than score 1 
			second = first#Keep first in variable second 
			first = num#keep variable num in first
		elif num > score2 and num != score1:#if num more than  score2 and num in not equal score1
			second = num#Keep value num in variable second

		average += (num/n_s)#Cal average score by average = average + (num/n_s)
	print("---")#show text ---
	print("Max score is: %.2f"%first)#show Max score
	if first == second or second == 0:#if first equal second or second equal to 0 show none
		print("Runner up is: None")
	else:# if not
		print("Runner up is: %.2f"%second)#Show Runner up
	print("Average is: %.2f"%average)#show Average value
Cal_score()


