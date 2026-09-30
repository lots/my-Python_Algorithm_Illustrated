class FNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class FullTree:
	def __init__(self):
		self.root = None
		self.length = 0
		self.k = 0			#层数
		self.nodes = []		#树中所有节点的引用

	def addLayer(self):
		m = 2**(self.k-1)
		start = len(self.nodes)-m
		lst = self.nodes[start:]
		for item in lst:
			item.left = FNode(None)
			item.right = FNode(None)
			self.nodes.append(item.left)
			self.nodes.append(item.right)
		self.k += 1

	def add(self,data):

		if self.root!=None:
			node = self.root
			for i in range(self.length):
				if data<node.data:
					if node.left!=None:
						if node.left.data!=None:
							node = node.left
						else:
							node.left.data = data
							break
					else:
						#添加一整个下层
						self.addLayer()
						node.left.data = data
						break
				else:
					if node.right!=None:
						if node.right.data!=None:
							node = node.right
						else:
							node.right.data = data
							break
					else:
						#添加一整个下层
						self.addLayer()
						node.right.data = data
						break
		else:
			fnode = FNode(data)
			self.root = fnode
			self.nodes.append(fnode)
			self.k = 1
		self.length += 1

	#满二叉树的遍历
	def displayNode(self,node,lst):
		if node.left!=None and node.left.data!=None:
			self.displayNode(node.left,lst)
		lst.append(node.data)
		if node.right!=None and node.right.data!=None:
			self.displayNode(node.right,lst)
	def display(self):
		node = self.root
		lst = []
		self.displayNode(node,lst)
		return lst

tree = FullTree()
lst = [6,2,7,3,5,9,8,4]
for item in lst:
	tree.add(item)
print(len(tree.nodes))
print(tree.k)
print(tree.display())
