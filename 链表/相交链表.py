from 单向链表 import Snode

class CrossList:
	def __init__(self):
		self.phead = None
		self.length = 0
		self.other = None
	def append(self,data):
		node = Snode(data)
		if self.phead != None:
			pl = self.phead
			while pl.next!=None:
				pl = pl.next
			pl.next = node
		else:
			self.phead = node
		self.length += 1
		if self.other!=None:
			self.other.length += 1

	def appendNode(self,node):
		if self.phead!=None:
			pl = self.phead
			while pl.next!=None:
				pl = pl.next
			pl.next = node
		else:
			self.phead = node
		self.length += 1
		if self.other!=None:
			self.other.length += 1
	def cross(self,other,data):
		node = Snode(data)
		if self.other==None:
			self.appendNode(node)
			other.appendNode(node)
			self.other = other
			self.other.other = self

	def display(self):
		lst = []
		node = self.phead
		while node!=None:
			lst.append(node.data)
			node = node.next
		return lst

	#随机访问方法
	def getData(self,seqnum):
		if seqnum>=self.length:
			seqnum = self.length-1
		elif seqnum<0:
			seqnum = 0
		pl = self.phead
		n = 0
		while n<seqnum:
			pl = pl.next
			n += 1
		return pl.data

	#随机插入方法
	def insert(self,data,seq):
		if seq>self.length:
			seq = self.length
		elif seq<0:
			seq = 0
		node = Snode(data)
		if seq>0:
			pl = self.phead
			n  = 0
			while n<(seq-1):
				pl = pl.next
				n += 1
			node.next = pl.next
			pl.next = node
		else:
			node.next = self.phead
			self.phead = node
		self.length += 1
	#随机删除方法
	def remove(self,seq):
		if seq>=self.length:
			seq = self.length-1
		elif seq<0:
			seq = 0
		node = None
		if seq>0:
			pl = self.phead
			n = 0
			while n<(seq-1):
				pl = pl.next
				n += 1
			node = pl.next
			pl.next = node.next
			node.next = None
		else:
			node = self.phead
			self.phead = node.next
			node.next = None
		self.length -= 1
		return node.data
	#反转整个链表
	def rev(self):
		def reversal(node):
			if node.next!=None:
				nextNode = node.next
				reversal(nextNode)
				nextNode.next = node
			else:
				self.phead.next=None
				self.phead = node
		reversal(self.phead)
	#反转从n到m索引处的节点
	def passrev(self,n,m):
		pl = self.phead
		ii = 0
		if n>0:
			while ii<(n-1):
				pl = pl.next
				ii += 1
			startNode = pl.next
		else:
			startNode = self.phead
			ii = -1

		def reversal(node,ii):
			ii += 1
			if ii<m:
				nextNode = node.next
				reversal(nextNode,ii)
				nextNode.next = node
			else:
				startNode.next = node.next
				if n>0:
					pl.next = node
				else:
					self.phead = node

		reversal(startNode,ii)

a = CrossList()
b = CrossList()
a.append(2)
a.append(3)
a.append(8)
a.append(1)
b.append(5)
b.append(6)
a.cross(b,10)
a.append(100)
a.append(1000)
print(a.display())
print(b.display())

def getCross(a,b):
	pa = a.phead
	pb = b.phead
	while pa.next!=None:
		pa = pa.next
	while pb.next!=None:
		pb = pb.next
	if pa==pb:
		print('相交')
		alen = a.length
		blen = b.length
		diffV = abs(alen-blen)
		pa = a.phead
		pb = b.phead
		if diffV>0:
			if alen>blen:
				for i in range(diffV):
					pa = pa.next
				slen = alen
			else:
				for i in range(diffV):
					pb = pb.next
				slen = blen
			for i in range(diffV,slen):
				if pa!=pb:
					pa = pa.next
					pb = pb.next
				else:
					print('相交点:',pa.data)
					break

	else:
		print('不相交')

getCross(a,b)