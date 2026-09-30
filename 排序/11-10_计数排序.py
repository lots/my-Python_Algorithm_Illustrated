def sort(a):
	n = len(a)
	m = max(a)
	b = [0]*(m+1)
	for i in a:
		b[i] += 1
	return b

arr = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]
rs = sort(arr)
print(rs)
m = max(arr)
for i in range(m+1):
	m = rs[i]
	for n in range(m):
		print(i,end=' ')