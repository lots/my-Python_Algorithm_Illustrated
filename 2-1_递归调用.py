def forFun(i):
	if i<10:
		forFun(i+1)
		print(i)
		#forFun(i+1)		#尾递归

forFun(1)