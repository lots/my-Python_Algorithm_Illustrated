from 栈结构.node import Node
class Stack:
	def __init__(self):
		self.point=None
		self.length=0
		self.name = None
	def push(self,value):
		node = Node(value)
		if self.point != None:
			node.pre = self.point
		self.point = node
		self.length += 1

	def pop(self):
		if self.point!=None:
			node = self.point
			self.point = node.pre
			node.pre = None
			self.length -= 1
			return node.value
		else:
			return None

	def isNone(self):
		if self.length>0:
			return False
		else:
			return True

a = Stack()					#声明1个栈
a.name = 'A'				#第1根柱子起名叫A
b = Stack()					#声明b柱子
b.name = 'B'
c = Stack()					#声明c柱子
c.name = 'C'

def move(n,s1,s2,s3):
	if n>1:
		move(n-1,s1,s3,s2)
		move(1,s1,s2,s3)
		move(n-1,s2,s1,s3)
	else:
		s3.push(s1.pop())		#把盘子移动到目标柱子上
		print(s1.name,'=>',s3.name)

for ii in range(4,0,-1):			#向a柱上压上4,3,2,1四个盘子
    a.push(ii)
n = a.length
move(n,a,b,c)

for ii in range(n):			#打印出c柱上的盘子编号
    print(c.pop())



