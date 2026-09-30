arr = [49,27,65,97,76,12,38]
alen = len(arr)
point = None
for i in range(alen):
	point = i
	for j in range(i+1,alen):
		if arr[point]>arr[j]:
			point = j
	temp = arr[i]
	arr[i] = arr[point]
	arr[point] = temp

print(arr)