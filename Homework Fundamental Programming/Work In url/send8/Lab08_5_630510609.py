#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab08_5
def decode(code_table, text):#Define decode function 
	cut = text.split("\n")#keep text.split newline in cut 
	for i in cut:#Loop in cut variable for remove space and ""
		if i.isspace():
			cut.remove(i)
		if i == "":
			cut.remove(i)
	for i in cut:#Loop in cut to remove whitespace
		cut = i.split(" ")
		for j in cut:#Loop in cut
			if j.startswith("-") or j.isdigit():#if j start - or is digits set j to integer and keep in x variable
				x = int(j)
				if x < 0 or x >= len(code_table):#if x less than 0 or more than equak to len of code_table print _ else print code_table pos [x]
					print("_" , end="")
				else:
					print(code_table[x],end="")
		print("")#print new line

def main():
	decode("aceiklmr-",'''
	3
	5 3 4 2
	3 1 2 8 1 7 2 0 86
	''')

if __name__ == "__main__":
	main()