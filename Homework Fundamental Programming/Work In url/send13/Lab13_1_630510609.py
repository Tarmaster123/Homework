#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab13_1
def count_segment(list_a):
	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0

	for i in list_a:
		d = (i[0]**2 + i[1]**2)**0.5
		#print("i : " , i )
		#print("q1 = ",q1)
		#print("q2 = ",q2)
		#print("q3 = ",q3)
		#print("q4 = ",q4)
		if i[0] >= 0 and i[1] >= 0:
			q1 += 1
			if i[0] - i[2] < 0:
				q2 += 1
			if i[1] - i[2] < 0:
				q4 += 1
			if i[2] > d:
				q3 += 1
			#print("q1 = ",q1)
			#print("q2 = ",q2)
			#print("q3 = ",q3)
			#print("q4 = ",q4)
		elif i[0] <= 0 and i[1] <= 0:
			q3 += 1
			if i[0] + i[2] > 0:
				q4 += 1
			if i[1] + i[2] > 0:
				q2 += 1
			if i[2] > d:
				q1 += 1
			#print("q1 = ",q1)
			#print("q2 = ",q2)
			#print("q3 = ",q3)
			#print("q4 = ",q4)
		elif i[0] >= 0 and i[1] <= 0:
			q4 += 1
			if i[0] - i[2] < 0:
				q3 += 1
			if i[1] + i[2] > 0:
				q1 += 1
			if i[2] > d:
				q2 += 1
			#print("q1 = ",q1)
			#print("q2 = ",q2)
			#print("q3 = ",q3)
			#print("q4 = ",q4)
		elif i[0] <= 0 and i[1] >= 0:
			q2 += 1
			if i[0] + i[2] > 0:
				q1 += 1
			if i[1] - i[2] < 0:
				q3 += 1
			if i[2] > d:
				q4 += 1
			#print("q1 = ",q1)
			#print("q2 = ",q2)
			#print("q3 = ",q3)
			#	print("q4 = ",q4)

	return q1,q2,q3,q4

def main():

	list_a = [(2, 7, 1.5),		#a
			(3.2, 2.5, 4.06),	#b
			(-5.5, -4.5, 2.5),	#c
			(2, -5.2, 3),		#d
			(7.2, -2.8, 1.2)] 	#e
	print(count_segment(list_a))

if __name__ == "__main__":
	main()
