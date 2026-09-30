
def f(n):
	if n>1:
		a = 1
		b = 1
		fibN = 0	#第n个斐波那契数列的存储单元
		for i in range(2,n+1):
			fibN = a+b
			a = b
			b = fibN
		return fibN
	else:
		return 1

for i in range(10):
	print(f(i))