def MergeSort(lst):
	alen = len(lst)
	if alen<=1:
		return lst
	num = int(alen/2)
	left = MergeSort(lst[:num])
	right = MergeSort(lst[num:])
	return Merge(left,right)

def Merge(left,right):
	l,r = 0,0
	result = []
	while l<len(left) and r<len(right):
		if left[l]<=right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1

	result += list(left[l:])
	result += list(right[r:])
	return result

arr = [8,4,5,7,1,3,9,6,2]

print(MergeSort(arr))