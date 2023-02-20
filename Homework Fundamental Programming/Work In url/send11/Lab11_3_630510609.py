#630510609
#กฤตเฒธ ไทยเจริญ
#003
#Lab11_3
def is_magic_square(board):#Define function is_magic_square to check is square magic
	#Create list to keep list each line 
	list_row_keep = []
	list_col_keep = []
	list_crossr_keep = []
	list_crossl_keep = []
	list_row = []
	list_col = []
	list_crossl = []
	list_crossr = []
	#Create list to keep list sum of digit
	sumA = []
	sumB = []
	sumC = []
	sumD = []
	#Create list to keep max of num of square
	max_ = []
	for rows in range(len(board)):#Loop for row in square
		for cols in range(len(board[0])):#Loop for col in square
			list_row.append(board[rows][cols])#keep board pos [rows][cols] in list_row
			list_col.append(board[cols][rows])#keep board pos [cols][rows] in list_col
			list_crossl.append(board[cols][cols])#keep board pos [cols][cols] in list_cross left
			if rows + cols == len(board) - 1:# if sum of rows and cols equal len of board - 1 keep board pos [rows][cols] in list_crossr
				list_crossr.append(board[rows][cols])
			else:
				continue
		list_row_keep.append(list_row)#keep list_row in list list_row_keep
		list_col_keep.append(list_col)#keep list_col in list list_col_keep
		list_crossl_keep.append(list_crossl)#keep list_crossl in list list_crossl_keep
		list_crossr_keep.append(list_crossr)#keep list_crossr in list list_crossr_keep
		list_row= []#reset list list_row
		list_col= []#reset list list_col
		list_crossl = []#reset list list_crossl
	for num1 in list_row_keep:#Check num in list_row_keep
		sumA.append(sum(num1))#keep sum in num1 in list sumA 
	for num2 in list_col_keep:#Check num in list_col_keep
		sumB.append(sum(num2))#keep sum in num2 in list sumB 
	for num3 in list_crossl_keep:#Check num in list_crossl_keep
		sumC.append(sum(num3))#keep sum in num3 in list sumC 
	for num4 in list_crossr_keep:#Check num in list_crossr_keep
		sumD.append(sum(num4))#keep sum in num4 in list sumD
		#Check num in square if num more than max_ return False 
	for rows in range(len(board)):
		for cols in range(len(board[0])):
			max_.append(board[rows][cols])
		for i in max_:
			if i > len(board) ** 2:
				return False
	if sumA == sumB == sumC == sumD  and num1 != num2 != num3 != num4:#If sumA equal to sumB sumC sumD and num1 not equal to num2 num3 num 4 return True else return False 
			return True
	else:
		return False

def main():
	board = [[2, 7, 6],[9, 5, 1],[4, 3, 8]]
	print(is_magic_square(board))

if __name__ == "__main__":
	main()
