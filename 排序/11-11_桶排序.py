bucket = [10,20,30,40,50]
bucketlst = []
for i in range(6):
	bucketlst.append([])

#桶中排序方法，插入排序
def insertSort(arr,v):
	arr.append(v)
	alen = len(arr)
	for i in range(alen-1,0,-1):
		if arr[i]<arr[i-1]:
			temp = arr[i]
			arr[i] = arr[i-1]
			arr[i-1] = temp
#入桶方法
def enterBucket(num):
	global bucket,bucketlst
	i = 0
	for v in bucket:
		if num<v:
			break
		i += 1
	insertSort(bucketlst[i],num)

#测试
arr = [31,25,43,9,27,18,5,44,38,26,17,34,1,8,48,13,79,7]
for v in arr:
	enterBucket(v)
print(bucketlst)
lst = []
for clst in bucketlst:
	lst += clst
print(lst)
