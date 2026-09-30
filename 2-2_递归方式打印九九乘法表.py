
def multiplication(n):
	if n<10:
		for m in range(1,n+1):
			print("%d*%d=%d"%(m,n,m*n),end="\t")
		print()
		multiplication(n+1)

multiplication(1)