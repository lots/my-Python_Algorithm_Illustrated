from 单向链表 import Snode

class ScLinkList:
	def __init__(self):
		self.phead = None
		self.length = 0
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

scList = ScLinkList()
for i in range(10):
	scList.append(i)
lst = scList.display()
print(lst)