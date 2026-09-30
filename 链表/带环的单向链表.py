from 单向链表 import Snode

class SlinkedCList:
	def __init__(self):
		self.phead = None
		self.length = 0
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
	#设置环
	def setCircle(self,n):
		if n>self.length or n<0:
			return False
		if self.length>3:
			pl = self.phead
			for i in range(n):
				pl = pl.next
			node = pl
			while pl.next!=None:
				pl = pl.next
			pl.next = node
			print('链接n节点:',node.data)
			return True
		else:
			return False

		
linkList = SlinkedCList()
for i in range(10):
	linkList.append(i)

def judgeCircle(linkList):
	fast = linkList.phead
	slow = linkList.phead
	while fast!=None and fast.next!=None:
		fast = fast.next.next
		slow = slow.next
		if fast==slow:
			print('有环')
			break
	if fast==None or fast.next==None:
		print('无环')
	else:
		slow = linkList.phead
		while slow!=fast:
			fast = fast.next
			slow = slow.next
		print('相会点:',slow.data)

judgeCircle(linkList)

linkList.setCircle(3)

judgeCircle(linkList)


