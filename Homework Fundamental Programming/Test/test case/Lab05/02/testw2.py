#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab05_2

#Define is_p_triple function for check. Is three of side Pythagorean triple? 
def is_p_triple(a, b, c):
#If c multiply by it self is equal to sum of a multiply by it self and b multiply by it self, if it balance return True.
	if c**2 == a**2 + b**2:
		return True
#But not in first condition check in second condition is b multiply by it self is equal to sum of c multiply by it self and a multiply by it self, if it balance return True.
	elif b**2 == c**2 + a**2:
		return True
#But not in seconds condition check in third condition is a multiply by it self is equal to sum of c multiply by it self and b multiply by it self, if it balance return True.
	elif a**2 == c**2 + b**2:
		return True
#But not at all return False.
	else:
		return False


def main():
	assert(is_p_triple(4, 5, 3) == True)
	assert(is_p_triple(42, 9, 41) == False)
	print("Pass all")

main()