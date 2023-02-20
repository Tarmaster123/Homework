#630510609
#กฤตเฒธ ไทยเจริญ
#003
#Lab11_1
def matrix_mult(m1, m2):#Define matrix_mult function to multiplication between m1 and m2 matrix
	result = [[0 for row in range(len(m2[0]))] for col in range(len(m1))]#use list comprehension to loop foe create list to keep result in variable result
	if len(m2) != len(m1[0]):#if row not equal to colum return None
		return
	else:
		for i in range(len(m1)):#Loop for row in m1
			for j in range(len(m2[0])):#Loop for each numberin m2
				for k in range(len(m1[0])):#Loop for each number in m1
					result[i][j] += m1[i][k] * m2[k][j] #m1 pos [i][j] multipy m2 pos[k][j]
		return result 


def main():
	m1 = [[1, 2, 3],[4, 5, 6]]
	m2 = [[7, 8],[9, 10],[11,12]]
	print(matrix_mult(m1, m2))
if __name__ == "__main__":
	main()