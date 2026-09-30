
num1 = [1,2,2,1,5,3,7]
num2 = [2,6,7,2]
arrShort = num1
arrLong = num2
if len(num2)<len(num1):
	arrShort = num2
	arrLong = num1

#把短数组中的值放进字典
dct = {}
for v in arrShort:
	if v not in dct.keys():
		dct[v] = 1

#遍历长数组
for v in arrLong:
	if v in dct.keys():
		dct[v] += 1

#找交集
for key in dct:
	if dct[key]>1:
		print(key)