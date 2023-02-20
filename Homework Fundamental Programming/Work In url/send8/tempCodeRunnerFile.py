			jn -= 1
	print()
	#create last line in square frame by start jn stop jn * 2 step -1
	for k in range(jn , (jn * 2 ) - 1 , -1):
		if k == (jn * 2):
			print(keep_num[k])
		else:
			print(keep_num[k] , end=sep)