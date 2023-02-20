#Define is_overlapped function for check is regtangle overlapped?
def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
	# l is length , t is tp , w = width , h = height
	#If lenght2 more than leght1.
	if l2 > l1:
		#If top2 more than top1.
		if t2 > t1:
			#If top2 more than sum of top1 and height1:
			if t2 > t1 + h1:
				#If sum of top2 and height2 more than sum of top1 and height.So It isn't overlappe return it to False
				if t2 + h2 > t1 + h1:
					return False
				#But not it is overlappe return it to True
				else:
					return True
			#But not
			else:
				#If lenght2 more than sum of lenght1 and width1.
				if l2 > l1 + w1:
					#If sum of lenght2 and width2 more than sum of length1 and width1.So It isn't overlappe return it to False
					if l2 + w2 > l1 + w1:
						return False
					#But not it is overlappe return it to True
					else:
						return True
				#But not.So it is overlappe return it True 
				else:
					return True
		#But not in first condition. Check top2 equal top1? 
		elif t2 == t1:
			#If sum of length1 and width less than length2.So It isn's overlappe return it to False
			if l1 + w1 < l2:                 
				return False 
			#But not.So it is overlappe return it to True               
			else:                                 
				return True
		#But not at all.       
		else:
			#If sum of top2 and height2 more than top1.
			if t2 + h2 > t1:
				#If sum of length1 and width less than length.So it isn't overlappe return it to False. 
				if l1 + w1 < l2:
					return False 
				#But not.So it is overlappe return it to True               
				else:
					return True
			#But not.
			else:
				#If sum of length1 and width less than length2.So it isn't overlappe return it to False
				if l1 + w1 < l2:
					return False
				#But not.
				else:
					#If sum of top2 and heigth2 less than top1.So it isn't overlappe return it to False
					if t2 + h2 < t1:
						return False
					#But not.So it is overlappe return it to True
					else:
						return True
	#But not.It is length2 less than length1. 
	else:
		#If top2 more than top1.
		if t2 > t1:
			#If top 2 more than sum of top1 and height.
			if t2 > t1 + h1:
				#If sum of top2 and heigth2 more than top1 and heigth1.So it isn't overlappe return it to False.
				if t2 + h2 > t1 + h1:
					return False
				#But not.So it is overlappe return it to True
				else:
					return True
			#But not.
			else:
				#If sum of length2 and width2 less than length1.So it isn't overlappe return it to False
				if l2 + w2 < l1:
					return False
				#But not.So it is overlappe return it to True
				else:
					return True
		#But not in first condition check top2 eqaul top1?
		elif t2 == t1:
			#If sum of length2 and width2 less than length1.So it isn't overlappe return it to False. 
			if l2 + w2 < l1:
				return False
			#But not.So it is overlappe return it to True.
			else:
				return True
		#But not at all.
		else:
			#If sum of length2 and width2 less than length1.So it isn't overlappe return it to False.
			if l2 + w2 < l1:
				return False
			#But not.
			else:
				#If sum of top2 and heigth2 less than top1.So it isn't overlappe return it to False. 
				if t2 + h2 < t1:
					return False
				#But not.So it is overlappe return it to True.
				else:
					return True
		
	#In addition to it is overlappe return it to True				
	return True


def main():              #l1   t1  w1   h1  l2    t2   w2   h2
	assert(is_overlapped(150 ,100 ,250 ,200 ,250 ,50 ,100 ,50) == True)
	#assert(is_overlapped(50 ,50 ,150 ,200 ,250 ,50 ,50 ,100) == False)
	#assert(is_overlapped(50 ,200 ,150 ,100 ,400 ,200 ,250 ,250) == False)
	#assert(is_overlapped(200 ,100 ,50 ,50 ,300 ,50 ,100 ,50) == False)


if __name__ == "__main__":
	main()
	


