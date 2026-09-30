lst = [8,9,3,3,7,3,5,3,7,3,8,3,3,2,3,6,3,1,3,0,3,6,3,9,3,3,8,3,5,3,2,3,1,2,3,4,3,7]
key = None
n = 0
for v in lst:
	if key!=None:
		if key == v:
			n += 1
		else:
			n -= 1
			if n==0:
				key = None
	else:
		key = v
		n = 1

if n>0:
	print('超过半数的值是:',key)