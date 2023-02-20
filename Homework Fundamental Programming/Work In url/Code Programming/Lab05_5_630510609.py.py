#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab05_5

#Define zodiac_element function to check zodiac and element from year.
def zodiac_element(year):
	#Set y equal to year modular 12 to find zodiac
	y = year % 12
	#Set ele equal to year modular 10 to find element
	ele = year % 10
	#If y equal to 0 zodiac is Monkey and keep it in variable zodiac. 
	if y == 0:
		zodiac = ("Monkey")
	#But not enter in first condition check y equal to 1 zodiac is Rooster and keep it in variable zodiac.
	elif y == 1:
		zodiac = ("Rooster")
	#But not enter in second condition check y equal to 2 zodiac is Dog and keep it in variable zodiac.
	elif y == 2:
		zodiac = ("Dog")
	#But not enter in Third condition check y equal to 3 zodiac is Pig and keep it in variable zodiac.
	elif y == 3:
		zodiac = ("Pig")
	#But not enter in fourth condition check y equal to 4 zodiac is Rat and keep it in variable zodiac.
	elif y == 4:
		zodiac = ("Rat")
	#But not enter in fifth condition check y equal to 5 zodiac is Ox and keep it in variable zodiac.
	elif y == 5:
		zodiac = ("Ox")
	#But not enter in sixth condition check y equal to 6 zodiac is Tiger and keep it in variable zodiac.
	elif y == 6:
		zodiac = ("Tiger")
	#But not enter in seventh condition check y equal to 7 zodiac is Rabbit and keep it in variable zodiac.
	elif y == 7:
		zodiac = ("Rabbit")
	#But not enter in eighth condition check y equal to 8 zodiac is Dragon and keep it in variable zodiac.
	elif y == 8:
		zodiac = ("Dragon")
	#But not enter in ninth condition check y equal to 9 zodiac is Snake and keep it in variable zodiac.
	elif y == 9:
		zodiac = ("Snake")
	#But not enter in tenth condition check y equal to 10 zodiac is Horse and keep it in variable zodiac.
	elif y == 10:
		zodiac = ("Horse")
	#But not at all zodiac is Goat and keep it in variable zodiac.
	else:
		zodiac = ("Goat")
	#If ele equal to 0 or 1 element is Metal and keep it in variable element.
	if ele == 0 or ele == 1:
		element = ("Metal")
	#But not enter in first condition check ele equal to 2 or 3 element is Water and keep it in variable element.
	elif ele == 2 or ele == 3:
		element = ("Water")
	#But not enter in second condition check ele equal to 4 or 5 element is Wood and keep it in variable element.
	elif ele == 4 or ele == 5:
		element = ("Wood")
	#But not enter in third condition check ele equal to 6 or 7 element is Fire and keep it in variable element.	
	elif ele == 6 or ele == 7:
		element = ("Fire")
	#But not at all element is Earth and keep it in variable element.
	else:
		element = ("Earth")
	#Return element and zodiac in string
	return ("%s %s" %(element,zodiac))

def main():
	year = int(input(""))
	print(zodiac_element(year))

if __name__ == '__main__':
	main()



