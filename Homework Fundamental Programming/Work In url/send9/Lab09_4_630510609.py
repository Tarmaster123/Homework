#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab9_04
def series(n):#define series(n) function to find number of series
	if n == 0 :#first base case if n equal to 0 return 0
		return 0
	if n == 1:#second base case if n equal to 1 return 1
		return 1
	else:
		if n % 2 == 0:#combine if num is even
			return 2*series(n-1) + 1#divide and conquer by decrease n and combine it to 2*series(n-1) + 1
		else:#combine id num is odd
			return 2*series(n-1) - 1##divide and conquer by decrease n and combine it to 2*series(n-1) - 1
def main():
	n = int(input("Input Your num: "))
	print(series(n))


if __name__ == "__main__":
	main()


"""
คู่ 2*series(n-1) + 1
คี่ 2*series(n-1) - 1
"""