class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class Quence:
	def __init__(self):
		self.head = None
		self.rear = None
		self.length = 0

	def inQue(self,value):
		node = Node(value)
		if self.head!=None:
			self.rear.next = node
			self.rear = node
		else:
			self.head = node
			self.rear = node
		self.length += 1

	def outQue(self):
		node = self.head
		if node.next!=None:
			self.head = node.next
			node.next = None
		else:
			self.head = None
			self.rear = None
		self.length -= 1
		return node.value

	def isNone(self):
		if self.head!=None:
			return False
		else:
			return True

quence = Quence()
for ii in range(10):
	quence.inQue(ii)

for ii in range(quence.length):
	print(quence.outQue())