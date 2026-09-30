class FNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class CompleteTree:
	def __init__(self):
		self.root = None
		self.length = 0
		self.k = 0
		self.nodes = []

	def supplyNodes(self,lst,curNode):
		for pnode in lst:
			if pnode.left!=curNode:
				if pnode.left==None:
					pnode.left = FNode(None)
			else:
				break
			if pnode.right!=curNode:
				if pnode.right==None:
					pnode.right=FNode(None)
			else:
				break

	def add(self,data):
		if self.root!=None:
			node = self.root
			lst1 = [self.root]
			lst2 = []
			while node!=None:
				if data<node.data:
					if node.left!=None:
						if node.left.data!=None:
							node = node.left
						else:
							node.left.data = data
							break
					else:
						node.left = FNode(data)
						#补满左侧节点
						self.supplyNodes(lst1,node.left)
						self.k += 1
						break
				else:
					if node.right!=None:
						if node.right.data!=None:
							node = node.right
						else:
							node.right.data = data
							break
					else:
						node.right = FNode(data)
						#补满左侧节点
						self.supplyNodes(lst1,node.right)
						self.k += 1
						break
				#补充上一层节点的空处
				for pnode in lst1:
					if pnode.left==None:
						pnode.left = FNode(None)
					lst2.append(pnode.left)
					if pnode.right==None:
						pnode.right = FNode(None)
					lst2.append(pnode.right)
				lst1 = lst2
				lst2 = []

		else:
			self.root = FNode(data)
			self.k += 1
			self.nodes.append(self.root)
		self.length += 1

	#遍历
	def diplayNode(self,node,lst):
		if node.left!=None and node.left.data!=None:
			self.diplayNode(node.left,lst)
		lst.append(node.data)
		if node.right!=None and node.right.data!=None:
			self.diplayNode(node.right,lst)

	def display(self):
		node = self.root
		lst = []
		self.diplayNode(node,lst)
		return lst

	#按层遍历
	def getNodes(self):
		lst1 = []
		lst2 = []
		nodes = []
		lst1.append(self.root)
		for i in range(self.k):
			nodes.append(lst1)
			for pnode in lst1:
				if pnode.left!=None:
					lst2.append(pnode.left)
				else:
					break
				if pnode.right!=None:
					lst2.append(pnode.right)
				else:
					break
			lst1 = lst2
			lst2 = []
		return nodes

tree = CompleteTree()
lst = [6,2,7,3,5,9,8,4]
for item in lst:
	tree.add(item)
print(tree.display())
print('---------------------------')
nodes = tree.getNodes()
for item in nodes:
	for node in item:
		print(node.data,end=' ')
	print('')
