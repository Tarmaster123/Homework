#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab10_2
def classify(list_x):#define classify for classify type input by user
	list_a = []#int
	list_b = []#float
	list_c = []#str
	x = []#keep value
	for i in list_x:#check each value in list_x 
		x += [i]#keep each value in x
	for j in x:
		if isinstance(j,int):#if value is int keep in list_a
			list_a += [j]
		elif isinstance(j,float):#if value is float keep in list_b
			list_b += [j]
		elif isinstance(j,str):#if value is str keep in list_c
			list_c += [j]
	return list_a , list_b , list_c#return tuple

def main():
	s = [10, 'hello', 23.5, 4]
	for i in classify(s):
		print(i)
if __name__ == "__main__":
	main()
'''
print(isinstance(23.5,int))
'''