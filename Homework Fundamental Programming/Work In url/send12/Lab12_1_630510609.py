def sort_date(list_x):
	for date in list_x:
		day = date[0:2]
		month = date[3:4]
		year = int(date[5:10])
		print(day)
		print(month)
		print(year)


		

	
def main():
	list_x =["11/1/2100","5/12/1999","19/1/2003","11/9/2001"]
	sort_date(list_x)

main()