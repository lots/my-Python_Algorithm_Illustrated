lst = [1,38,29,47,12,6,21,33,17,39]
lenLst = len(lst)
max = None
second = None
for v in lst:
	if max!=None:
		if max<v:
			temp = max
			max = v
			second = temp
		else:
			if second!=None:
				if second<v:
					second=v
			else:
				second = v
	else:
		max = v

print(max,',',second)