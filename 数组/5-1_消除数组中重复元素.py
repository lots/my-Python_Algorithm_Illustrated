lst = [1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5]
lenLst = len(lst)
i = 0
while i<lenLst:
	v = lst[i]
	j = i+1
	while j<lenLst:
		if v == lst[j]:
			del lst[j]
			j -= 1
			lenLst -= 1
		j += 1
	i += 1

print(lst)