bucketlst = []
for i in range(10):
	bucketlst.append([])

def radixSort(arr):
	global bucketlst
	max_num = max(arr)
	m = 0
	while max_num>10**m:
		m += 1

	for n in range(m):
		for v in arr:
			k = (int(v/(10**n)))%10
			bucketlst[k].append(v)
		i=0
		for clst in bucketlst:
			for v in clst:
				arr[i] = v
				i += 1
			clst.clear()

#测试
arr = [12,3,45,2543,214,1,10,4553,121]
radixSort(arr)
print(arr)