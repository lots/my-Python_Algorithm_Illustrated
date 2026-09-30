lst = [9,-3,7,5,15,-9,5,4,-2]
fulcrums = []		#支点元素存储列表
lstLen = len(lst)
for v in range(1,lstLen-1):
	#左侧子数组求和
	leftSum = 0
	for i in range(0,v):
		leftSum += lst[i]
	#右侧子数组求和
	rightSum = 0
	for j in range(v+1,lstLen):
		rightSum += lst[j]
	if leftSum == rightSum:
		fulcrums.append(v)

print('支点元素是:',fulcrums)