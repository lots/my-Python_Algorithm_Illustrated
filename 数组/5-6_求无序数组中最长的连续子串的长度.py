lst = [13,5,9,3,4,5,43,2,7,5,9,10,11,12,13,24,6,17,9]
preV = None
n = 0
max = 0
for v in lst:
	if preV!=None:
		preV += 1
		if preV==v:
			n += 1
		else:
			preV = v
			if n>max:
				max = n
			n = 1
	else:
		preV = v
		n = 1

print('最长子串:',max)