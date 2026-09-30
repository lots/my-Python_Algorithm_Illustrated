from 栈结构.stack import Stack
stack = Stack()

def rev(node):
	global stack
	preNode = node.pre
	if preNode!=None:
		rev(preNode)
		preNode.pre = node
	else:
		stack.point = node
for i in range(1,6):
	stack.push(i)
node = stack.point
rev(node)
node.pre = None
for i in range(stack.length):
	print(stack.pop())