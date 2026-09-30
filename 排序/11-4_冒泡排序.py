arr = [6,3,8,2,9,1]
alen = len(arr)
temp = None
for i in range(alen):
	for j in range(0,alen-1-i):
		if arr[j]>arr[j+1]:
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp

print(arr)
