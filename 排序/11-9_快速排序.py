
def quicksort(left,right):
	if left>=right:
		return
	temp = arr[left]
	i = left
	j = right

	while i!=j:
		#找右侧小于基准数的元素
		while arr[j]>=temp and i<j:
			j -= 1

		while arr[i]<=temp and i<j:
			i += 1

		if i<j:
			t = arr[i]
			arr[i] = arr[j]
			arr[j] = t

	arr[left] = arr[i]
	arr[i] = temp

	quicksort(left,i-1)
	quicksort(i+1,right)

arr = [8,4,5,12,7,1,3,6,2]
n = len(arr)-1
quicksort(0,n)
print(arr)