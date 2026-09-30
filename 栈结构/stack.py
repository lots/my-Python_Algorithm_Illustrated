#import sys 
#sys.path.append('../')		#返回上一级目录时用

from 栈结构.node import Node
class Stack:
	def __init__(self):
		self.point = None
		self.length = 0
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