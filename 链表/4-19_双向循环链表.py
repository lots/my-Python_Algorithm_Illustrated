from 双向链表 import DulNode

class DuLoopLink:
	def __init__(self):
		self.phead = None
		self.ptail = None
		self.length = 0
	def append(self,data):
		node = DulNode(data)
		if self.phead!=None:
			self.ptail.next = node
			node.pre = self.ptail
			node.next = self.phead
			self.phead.pre = node
			self.ptail = node
		else:
			node.next = node
			node.pre = node
			self.phead = node
			self.ptail = node
		self.length += 1

	def display(self):				#正向遍历
		lst = []
		node = self.phead
		for i in range(self.length):
			lst.append(node.data)
			node = node.next
		return lst

	def reDisplay(self):
		lst = []
		node = self.ptail
		for i in range(self.length):
			lst.append(node.data)
			node = node.pre
		return lst

	#随机插入
	def insert(self,data,seq):
		if seq>=self.length:		#插入尾部
			self.append(data)
			return
		elif seq<0:
			seq = 0
		node = DulNode(data)
		if seq>0:					#插入中间
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
			self.ptail.next = node
			node.pre = self.ptail
		self.length += 1

	#随机删除
	def remove(self,seq):
		node = None
		if self.length==0:
			return None
		if seq>=(self.length-1):		
			node = self.ptail
			if self.length>1:			#删除尾节点
				self.ptail = node.pre
				node.pre.next = self.phead
				self.phead.pre = node.pre
				node.pre = None
				node.next = None
			else:
				node.pre = None
				node.next = None
				self.phead = None
				self.ptail = None
			self.length -= 1
			return node.data
		elif seq<=0:							#删除头节点
			node = self.phead
			if self.length>1:
				self.phead = node.next
				self.phead.pre = self.ptail
				self.ptail.next = self.phead
				node.next = None
				node.pre = None
			else:
				node.pre = None
				node.next = None
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

duLoopLink = DuLoopLink()
for i in range(1,11):
	duLoopLink.append(i)

print(duLoopLink.display())
duLoopLink.remove(0)
duLoopLink.remove(5)
duLoopLink.remove(10)
print(duLoopLink.display())
duLoopLink.insert(100,5)
print(duLoopLink.display())
# print(duLoopLink.display())
# print(duLoopLink.reDisplay())
