from 单向链表 import Snode

class YcLinkList:
	def __init__(self):
		self.phead = None
		self.length = 0
		self.forPoint = None	#计数指针
		self.prePoint = None	#慢一步的指针
	def append(self,data):
		node = Snode(data)
		if self.phead!=None:
			pl = self.phead
			while pl.next!=self.phead:
				pl = pl.next
			node.next = pl.next
			pl.next = node
		else:
			self.phead = node
			node.next = node
		self.length += 1

	def display(self):
		lst = []
		node = self.phead
		lst.append(node.data)
		while node.next!=self.phead:
			node = node.next
			lst.append(node.data)
		return lst

	def yueNext(self):
		if self.length>2:
			if self.forPoint!=None:
				self.prePoint = self.forPoint
				self.forPoint = self.forPoint.next
			else:
				self.forPoint = self.phead
			return True
		else:
			return False

	def yueRemove(self):
		node = self.forPoint
		if node == self.phead:
			self.phead = node.next
		self.forPoint = self.forPoint.next
		self.prePoint.next = node.next
		node.next = None
		self.length -= 1
		print(node.data,'出队')

ycLinkList = YcLinkList()

for i in range(1,41):
	ycLinkList.append(i)

ii = 0
while ycLinkList.yueNext():
	ii += 1
	if ii==3:
		ycLinkList.yueRemove()
		ii = 1

print(ycLinkList.display())

