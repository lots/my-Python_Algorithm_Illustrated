class BinaryHeap:
	def __init__(self):
		self.body = [None]
		self.end = 0		#最长下标
	def add(self,data,n=0):
		if n>self.end:
			for i in range(self.end,n):
				self.body.append(None)
			self.end = n
		if self.body[n]!=None:
			if data<self.body[n]:
				self.add(data,2*n+1)
			else:
				self.add(data,2*n+2)
		else:
			self.body[n]=data

	def sort(self,arr,n):
		if n<=self.end:
			v = self.body[n]
			if v!=None:
				pLeft = 2*n+1
				self.sort(arr,pLeft)
				arr.append(v)
				pRight = 2*n+2
				self.sort(arr,pRight)

	def display(self):
		arr = []
		self.sort(arr,0)
		return arr

binaryHeap = BinaryHeap()
lst = [6,3,9,4,8,5]
for v in lst:
	binaryHeap.add(v)

#print(binaryHeap.body)
print(binaryHeap.display())