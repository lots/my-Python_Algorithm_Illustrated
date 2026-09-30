import math
arr = [8,9,1,7,2,10,3,5,4,6,0]
n = len(arr)
gap = math.ceil(n/2)
while True:
	for group in range(gap):
		for i in range(group,n,gap):
			for j in range(i,0,-gap):
				if arr[j]<arr[j-gap]:
					temp = arr[j]
					arr[j] = arr[j-gap]
					arr[j-gap] = temp

	if gap==1:
		break
	gap = math.ceil(gap/2)

print(arr)