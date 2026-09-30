from 栈结构.stack import Stack
class StackQue:
	def __init__(self):
		self.a = Stack()
		self.b = Stack()
	def appendTail(self,value):
		if self.b.isNone()==False:
			blen = self.b.length
			for i in range(blen):
				self.a.push(self.b.pop())
		self.a.push(value)

	def deleteHead(self):
		if self.b.isNone():
			alen = self.a.length
			for i in range(alen):
				self.b.push(self.a.pop())
		return self.b.pop()

stackque = StackQue()
for i in range(5):
	stackque.appendTail(i)
for i in range(2):
	print(stackque.deleteHead())
for i in range(7,10):
	stackque.appendTail(i)
for i in range(10):
	print(stackque.deleteHead())