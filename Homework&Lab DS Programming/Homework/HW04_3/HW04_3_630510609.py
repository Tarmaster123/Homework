#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# HW04_3
# 229223 Sec 002

def main():
    test_is_overlapped()

# def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
# 	if l2 > l1:
# 		if t2 > t1:
# 			if t2 > t1 + h1:
# 				if t2 + h2 > t1 + h1:
# 					return False
# 				else:
# 					return True
# 			else:
# 				if l2 > l1 + w1:
# 					if l2 + w2 > l1 + w1:
# 						return False
# 					else:
# 						return True
# 				else:
# 					return True
# 		elif t2 == t1:
# 			if l1 + w1 < l2:                 
# 				return False 
# 			else:                                 
# 				return True
# 		else:
# 			if t2 + h2 > t1:
# 				if l1 + w1 < l2:
# 					return False 
# 				else:
# 					return True
# 			else:
# 				if l1 + w1 < l2:
# 					return False
# 				else:
# 					if t2 + h2 < t1:
# 						return False
# 					else:
# 						return True
# 	else:
# 		if t2 > t1:
# 			if t2 > t1 + h1:
# 				if t2 + h2 > t1 + h1:
# 					return False
# 				else:
# 					return True
# 			else:
# 				if l2 + w2 < l1:
# 					return False
# 				else:
# 					return True
# 		elif t2 == t1:
# 			if l2 + w2 < l1:
# 				return False
# 			else:
# 				return True
# 		else:
# 			if l2 + w2 < l1:
# 				return False
# 			else:
# 				if t2 + h2 < t1:
# 					return False
# 				else:
# 					return True
# 	return True

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    lx1 = l1 + w1
    ty1 = t1 + h1

    lx2 = l2 + w2
    ty2 = t2 + h2

    if (lx1 == l1) or (t1 == ty1) or (lx2 == l2) or  (t2 == ty2):
        return False 

    if (l1 > lx2) or (l2 > lx1):
        return False

    if (t1 > ty2) or (t2 > ty1):
        return False 

    else:
        return True

def test_is_overlapped():
    assert(is_overlapped(10, 10, 50, 75, 30, 55, 60, 60)) == True
    assert(is_overlapped(10, 10, 50, 75, 70, 55, 60, 60)) == False
    print("OK EIei")

if __name__ =="__main__":
    main()