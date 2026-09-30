class MaxHeap:
	def __init__(self):
		self.body = []
		self.len = 0

	def add(self,data):
		self.body.append(data)
		if self.len>0:
			n = self.len
			if n>0:
				if n%2==1:
					pn = int((n-1)/2)
				else:
					pn = int((n-2)/2)
				while self.body[pn]<data:
					self.body[n] = self.body[pn]
					self.body[pn] = data
					n = pn
					if n>0:
						if n%2==1:
							pn = int((n-1)/2)
						else:
							pn = int((n-2)/2)
					else:
						break
		self.len += 1

	#调整堆顶数值在堆中的位置
	def setHeapTop(self,lst,n,lstLen):
		index = 0
		if n+1<lstLen:
			index = n+1
			if n+2<lstLen:
				if lst[n+2]>lst[index]:
					index = n+2
			if lst[n]<lst[index]:
				temp = lst[n]
				lst[n] = lst[index]
				lst[index] = temp
				self.setHeapTop(lst,index,lstLen)

	def display(self):
		lst = self.body[:]
		end = len(lst)
		while end>1:
			temp = lst[0]
			lst[0]=lst[end-1]
			lst[end-1]=temp
			end -= 1
			self.setHeapTop(lst,0,end)
			#print(lst)
		return lst


lst = [1,9,12,3,8,4,15]
maxHeap = MaxHeap()
for v in lst:
	maxHeap.add(v)

print(maxHeap.body)
lst1 = maxHeap.display()
print(lst1)

