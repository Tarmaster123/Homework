#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab11_2
def remove_row_col(list_a, row, col):#Define remove_row_col function to remove row and colum by user input
	list_b = []#Create list_b
	list_c = []#Create list_c
	if row < 0:# if row is negative 
		row += len(list_a)#do row positive by row = row + len(list_a)
		if col >= 0:#if colum is positive 
			for rows in range(len(list_a)):#Loop for row
				for cols in range(len(list_a[0])):#Loop for each number in row(colum) 
					if cols != col and rows != row:#keep number in row and colum except number row and colum input by user in list_b
						list_b.append(list_a[rows][cols])
				if rows == row:
					continue
				list_c.append(list_b)#Keep list_b in list_c
				list_b = []#Reset list_b
		else:#col is negative
			col += len(list_a[0])#do col positive by col = col + len(list_a[0])
			for rows in range(len(list_a)):#Loop for row
				for cols in range(len(list_a[0])):#Loop for each number in row(colum) 
					if cols != col and rows != row::#keep number in row and colum except number row and colum input by user in list_b
						list_b.append(list_a[rows][cols])
				if rows == row:
					continue
				list_c.append(list_b)#Keep list_b in list_c
				list_b = []#Reset list_b
	else:#row is positive
		if col >= 0:#if colum is positive 
			for rows in range(len(list_a)):#Loop for row
				for cols in range(len(list_a[0])):#Loop for each number in row(colum) 
					if cols != col and rows != row:#keep number in row and colum except number row and colum input by user in list_b
						list_b.append(list_a[rows][cols])
				if rows == row:
					continue
				list_c.append(list_b)#Keep list_b in list_c
				list_b = []#Reset list_b
		else:#col is negative
			col += len(list_a[0])#do col positive by col = col + len(list_a[0])
			for rows in range(len(list_a)):#Loop for row
				for cols in range(len(list_a[0])):#Loop for each number in row(colum) 
					if cols != col and rows != row:#keep number in row and colum except number row and colum input by user in list_b
						list_b.append(list_a[rows][cols])
				if rows == row:
					continue
				list_c.append(list_b)#Keep list_b in list_c
				list_b = []#Reset list_b
	return list_c#return list_c


def main():#  0  1  2  3  
	list_a =[[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]] 
	row = 1
	col = -3
	print(remove_row_col(list_a, row, col))
if __name__ == "__main__":
	main()
