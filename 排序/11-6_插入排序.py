arr = [7,3,15,1,23,6]
alen = len(arr)
for i in range(alen):
	for j in range(i,0,-1):
		if arr[j]<arr[j-1]:
			temp = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = temp
		else:
			break

print(arr)
