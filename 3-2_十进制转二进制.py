from 栈结构.stack import Stack
import math
def tenToTwo(n):
	if n>1:
		stack = Stack()
		temp = n
		while(temp>0):
			mod = temp%2
			stack.push(mod)
			temp = math.floor(temp/2)
		v = stack.pop()
		while(stack.isNone()==False):
			v = v*10+stack.pop()
		return v
	else:
		return n

print(tenToTwo(6))
print(tenToTwo(9))