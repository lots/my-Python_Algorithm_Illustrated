lst = [6,3,8,7,2,5,9,0,6,3,8,4,8,0,6,1,5,0,9,7,6,4]
preV = None
luckyV = 0
for v in lst:
	if preV!=0:
		if v==6 or v==8 or v==9:
			luckyV += 1
		elif v==4:
			luckyV -= 1
	else:
		if v==6 or v==8 or v==9:
			luckyV -= 1
		elif v==4:
			luckyV += 1
	preV = v

print('幸运值:',luckyV)