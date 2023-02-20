#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab05_3

#Define leap_yaer for check, Is year leapyear? 
def leap_year(y):
#If y modular 4 and 400 equal 0 year is leap year but must to not modular 100 equal 0. And return True if year is leap year and False if isn't. 
	if y%4 == 0:
		if y%400 == 0:
			return True
		elif y%100 == 0:
			return False
		else:
			return True
	else:
		return False
#Define leap_year_n for check, Is next year is leap year? By if variable y+1 and modular 4 and 400 equal 0 but must to not modular 100 equal 0. And return True if year is leap year and False if isn't.
def leap_year_n(y):
	if (y+1)%4 == 0:
		if (y+1)%400 == 0:
			return True
		elif (y+1)%100 == 0:
			return False
		else:
			return True
	else:
		return False
#Define connt_down_to_songkran for count down to next sonkran day.
def count_down_to_songkran(d, m, y):
#Fix each variable is each month. 
	J = 31# J is January have 31 day per month.
	F = 28# F is Febuary have 28 day per month.
	Fl = 29# Fl is Febuary in leap year have 29 day per month.
	M = 31# M is March have 31 day per month.
	A = 30# A is Arpil have 30 day per month.
	Ma = 31# Ma is May have 31 day per month. 
	Ju = 30# Ju is June have 30 day per month.
	Jl = 31# Jl is July have 31 day per month. 
	Au = 31# Au is August have 31 day per month.
	S = 30# S is September have 30 day per month.
	O = 31# O is October have 31 day per month.
	N = 30# N is November have 30 day per month.
	D = 31# D is December have 31 day per month.
#Calculate in case m(mont) is equal or less than 4.
	if m <= 4:
		#If m equal to 1
		if m == 1:
			#Check is it leap year?
			#If True take number per month in J minus start day(d) and plus sum of Fl , M and 13(Start day in songkran)
			if leap_year(y) == True:
				result = (J - d) + Fl + M + 13
			#But not True take number per month in J minus start day(d) and plus sum of F , M and 13(Start day in songkran)
			else:
				result = (J - d) + F + M + 13
		#If m equal to 2
		elif m == 2:
			#Check is it leap year?
			#If True take number per month in Fl minus start day(d) and plus sum of M and 13(Start day in songkran)
			if leap_year(y) == True:
				result = (Fl - d) + M + 13
			#But not take number per month in F minus start day(d) and plus sum of M and 13(Start day in songkran)
			else:
				result = (F - d) + M +13
		#If m equal to 3
		elif m == 3:
			#Take number per month in M minus start day(d) and plus 13(Start day in songkran) 
			result = (M - d) + 13
		#But not at all it is m equal to 4
		else:
			#If d equal 13 it's mean this day is songkran day so result equal 0.
			if d == 13:
				result = 0
			#But not in first condition take d minus 13 for calculate differnce between start day and 13 
			elif d < 13:
				result = abs(d - 13)
			#But not at all it is d more than 13 it's mean must waiting songkran day in next year.
			else:
				#If it is leap year?
				if leap_year_n(y) :
					#if d equal to 13 must to waiting to next year is 366 day
					if d == 13:
						result = 366 
					#But not take 366 minus difference of start day and 13
					else :
						result = 366 - abs(d - 13)
				#But not.
				else:
					#if d equal to 13 must to waiting to next year is 365 day 
					if d == 13:
						result = 365 
					#But not take 365 minus difference of start day and 13
					else:
						result = 365 - abs(d - 13)
		#Return all result
		return result
	#But not it is m may be equal to 5 , 6 , 7 , 8 , 9 , 10 , 11 or 12
	else:
		#Check is it leap year?
		if leap_year(y) == True:#True
			#Calculate number of day before next songkran day by take number per month minus start day and plus sum of all of month before songkran day.
			if m == 5:
				result = (Ma - d) + Ju + Jl + Au + S + O + N + D + J + F + M + 13
			elif m == 6:
				result = (Ju - d) + Jl + Au + S + O + N + D + J + F + M + 13
			elif m == 7:
				result = (Jl - d) + Au + S + O + N + D + J + F + M + 13
			elif m == 8:
				result = (Au - d) + S + O + N + D + J + F + M + 13
			elif m == 9:
				result = (S - d)  + O + N + D + J + F + M + 13
			elif m == 10:
				result = (O - d)  + N + D + J + F + M + 13
			elif m == 11:
				result = (N - d)  + D + J + F + M + 13
			else :
				result = (D - d)  + J + F + M + 13
			return result
		#But not. Check is next year leap year?
		else:
			if leap_year_n(y) == True :#True
				#Calculate number of day before next songkran day by take number per month minus start day and plus sum of all of month before songkran day and change F to Fl(Febuary in leap year).
				if m == 5:
					result = (Ma - d) + Ju + Jl + Au + S + O + N + D + J + Fl + M + 13
				elif m == 6:
					result = (Ju - d) + Jl + Au + S + O + N + D + J + Fl + M + 13
				elif m == 7:
					result = (Jl - d) + Au + S + O + N + D + J + Fl + M + 13
				elif m == 8:
					result = (Au - d) + S + O + N + D + J + Fl + M + 13
				elif m == 9:
					result = (S - d)  + O + N + D + J + Fl + M + 13
				elif m == 10:
					result = (O - d)  + N + D + J + Fl + M + 13
				elif m == 11:
					result = (N - d)  + D + J + Fl + M + 13
				else :
					result = (D - d)  + J + Fl + M + 13
				return result
			#But not. 
			else :
				#Calculate number of day before next songkran day by take number per month minus start day and plus sum of all of month before songkran day not to change F to Fl .
				if m == 5:
					result = (Ma - d) + Ju + Jl + Au + S + O + N + D + J + F + M + 13
				elif m == 6:
					result = (Ju - d) + Jl + Au + S + O + N + D + J + F + M + 13
				elif m == 7:
					result = (Jl - d) + Au + S + O + N + D + J + F + M + 13
				elif m == 8:
					result = (Au - d) + S + O + N + D + J + F + M + 13
				elif m == 9:
					result = (S - d)  + O + N + D + J + F + M + 13
				elif m == 10:
					result = (O - d)  + N + D + J + F + M + 13
				elif m == 11:
					result = (N - d)  + D + J + F + M + 13
				else :
					result = (D - d)  + J + F + M + 13
				return result 

def main():
	print(count_down_to_songkran(5 ,6 ,1997)  )
	print(count_down_to_songkran(5 ,6 ,1999) )

if __name__ == '__main__':
	main()

