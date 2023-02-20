#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab05_1

#Define Euclid_dis function for calculate distance between dot.
def Euclid_dis(x1,y1,r1,x2,y2,r2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5
	#Define intersects for consider circle that it is touching , none-intersecting or intersecting.
def intersects(x1,y1,r1,x2,y2,r2, epsilon=10**-6):
	#Keep Euclid_dis function in variable D. 
	D = Euclid_dis(x1,y1,r1,x2,y2,r2)
	#Consider that circle is touching by if  D - (r1 + r2) is between epsilon and -epsilon so result is 0.
	if D - (r1 + r2) <= epsilon and D - (r1 + r2) >= -epsilon:
		result = 0
	#But if D is more than sum of radius1 and radius2 so result is -1 it's mean this circle is non-intersecting.	
	elif D > r1 +r2 :
		result = -1
	#But if D is between range of radius1 and radius2, and sum of radius1 and radius2 it's mean this circle is intersecting so result is 1. 
	elif D > abs(r1-r2) and D < r1 + r2:
		result = 1
	#But not at all it's mean this circle is non intersecting and result is -1. 
	else:
		result = -1
	#Return result of all
	return result

def main():
	assert(intersects(83.14 ,51.69 ,10.54702915 ,43.25 ,41.96 ,30.5125) == 0 )#0 -1
	assert(intersects(2.82 ,69.42 ,1.559176989 ,19.21 ,69.09 ,22.9525) == -1 )#-1 1

if __name__ == '__main__':
	main()


	