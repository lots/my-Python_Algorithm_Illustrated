
def wheat(n):
	if n>1:
		sum,rs = wheat(n-1)
		rs = rs*2				#当前格子里应该有几粒麦子
		sum = sum + rs
		return sum,rs
	else:
		return 1,1

sum,rs = wheat(64)

print(sum)
