class DulNode:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.pre = None

class DuLinkList:
	def __init__(self):
		self.phead = None
		self.ptail = None
		self.length = 0

	def append(self,data):
		node = DulNode(data)
		if self.phead!=None:
			self.ptail.next = node
			node.pre = self.ptail
			self.ptail = node
		else:
			self.phead = node
			self.ptail = node

		self.length += 1

	#正向遍历
	def display(self):
		lst = []
		node = self.phead
		while node!=None:
			lst.append(node.data)
			node = node.next
		return lst
	#逆向遍历
	def revDisplay(self):
		lst = []
		node = self.ptail
		while node!=None:
			lst.append(node.data)
			node = node.pre
		return lst
	#随机插入
	def insert(self,data,seq):
		if seq>=self.length:
			self.append(data)
			return
		elif seq<0:
			seq = 0
		node = DulNode(data)
		if seq>0:
			pl = self.phead
			n = 0
			while n<(seq-1):
				pl = pl.next
				n += 1
			inode = pl.next
			pl.next = node
			node.pre = pl
			node.next = inode
			inode.pre = node
		else:
			node.next = self.phead
			self.phead.pre = node
			self.phead = node
		self.length += 1

	#随机删除
	def remove(self,seq):
		node = None
		if seq>=(self.length-1):
			seq = self.length-1
			node = self.ptail
			if node.pre!=None:
				self.ptail = node.pre
				node.pre.next = None
				node.pre = None
			else:
				self.phead = None
				self.ptail = None
			self.length -= 1
			return node.data
		elif seq<=0:
			seq = 0
			node = self.phead
			if node.next!=None:
				self.phead = node.next
				node.next.pre = None
				node.next = None
			else:
				self.phead = None
				self.ptail = None
			self.length -= 1
			return node.data
		pl = self.phead
		n = 0
		while n<seq:
			pl = pl.next
			n += 1
		node = pl
		node.pre.next = node.next
		node.next.pre = node.pre
		node.pre = None
		node.next = None
		self.length -= 1
		return node.data
	#插值法排序
	def insertBySort(self,data):
		node = DulNode(data)
		pl = self.ptail
		if pl!=None:
			while pl!=None and data<pl.data:
				pl = pl.pre
			if pl!=None:				#当链表不为空
				if pl!=self.ptail:		#从中间插入
					nextNode = pl.next
					pl.next = node
					node.pre = pl
					node.next = nextNode
					nextNode.pre = node
				else:					#从尾部插入
					pl.next = node
					node.pre = pl
					self.ptail = node
			else:						#从头部插入
				node.next = self.phead
				self.phead.pre = node
				self.phead = node
		else:							#当链表为空
			self.phead=node
			self.ptail=node

# dlink = DuLinkList()
# lst = [25,3,7,5,3,6,8,2,17,3,5,10,11]
# for i in lst:
# 	dlink.insertBySort(i)
# print(dlink.display())

# for i in range(10):
# 	dlink.append(i)
# print(dlink.display())
# #print(dlink.revDisplay())
# dlink.insert(100,5)
# dlink.insert(100,-3)
# dlink.insert(100,15)
# print(dlink.display())

# dlink.remove(5)
# dlink.remove(0)
# dlink.remove(13)
# print(dlink.display())