from stack import Stack
stack = Stack()
for ii in range(5):
	print(ii)
	stack.push(ii)

print(stack.isNone())
print('--------------------')
for ii in range(stack.length):
	print(stack.pop())
	
print(stack.isNone())