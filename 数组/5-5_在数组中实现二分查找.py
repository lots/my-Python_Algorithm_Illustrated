import math
lst = [3,5,9,13,17,22,25,29,33,36,41,43,44,48,49,56,61,67]
search = 29
lstLen = len(lst)
left = 0
right = lstLen-1
flag=0				#找到元素的标志位
while left<right:
	point = left + math.floor((right-left)/2)
	v = lst[point]
	if search<v:
		right = point
	elif search>v:
		left = point+1
	else:
		print('找到位置',point)
		flag=1
		break
if flag==0:
	print('没找到')