#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab08_3
def patterned_message(message, pattern):#Define patterned_message function to do message follow to pattern 
	x = 0#set x variable to 0
	cut = message.strip()#keep message.strip() in cut 
	for i in message:#Loop in message for change " " to ""
		if i == " ":
			message = message.replace(" ","")
	for i in pattern:#Loop in pattern
		if x == len(message):#if x equal to len of message set x to 0
			x = 0
		if i == "*":#if i is * change it to message pos [x] and x increase 1
			print(message[x] , end = "")
			x += 1
		if i == " ":#if i is " " print " "
			print(" ",end = "")
		if i == "\n":#if i is new line print new line
			print("")

def main():
	patterned_message("Three Diamonds!",'''
 * * *
 *** *** ***
 ***** ***** *****
 *** *** ***
 * * *
''')


if __name__ == "__main__":
	main()

