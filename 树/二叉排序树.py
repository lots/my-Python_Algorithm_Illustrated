class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add(self,node):
		if node.data<self.data:
			if self.left!=None:
				self.left.add(node)
			else:
				self.left = node
		else:
			if self.right!=None:
				self.right.add(node)
			else:
				self.right = node

	def display(self,lst):
		if self.left!=None:
			self.left.display(lst)
		lst.append(self.data)
		if self.right!=None:
			self.right.display(lst)


class SortTree:
	def __init__(self):
		self.root = None
		self.length = 0
	def add(self,data):
		snode = Node(data)
		if self.root!=None:
			self.root.add(snode)
		else:
			self.root = snode
		self.length += 1

	def display(self):
		lst = []
		self.root.display(lst)
		return lst

	#前序遍历
	def preOrder(self):
		lst = []
		node = self.root
		self.recursivePreOrder(node,lst)
		return lst
	#前序遍历递归方法
	def recursivePreOrder(self,node,lst):
		lst.append(node.data)
		if node.left!=None:
			self.recursivePreOrder(node.left,lst)
		if node.right!=None:
			self.recursivePreOrder(node.right,lst)

	#后序遍历
	def postOrder(self):
		lst=[]
		node = self.root
		self.recursivePostOrder(node,lst)
		return lst
	def recursivePostOrder(self,node,lst):
		if node.left!=None:
			self.recursivePostOrder(node.left,lst)
		if node.right!=None:
			self.recursivePostOrder(node.right,lst)
		lst.append(node.data)

	#广度优先遍历
	def levelTraverse(self):
		lst = []
		nodeLst = []		#层节点列表
		nodeLstTmp = []		#临时存放层节点列表
		if self.root!=None:
			nodeLst.append(self.root)
		while len(nodeLst)>0:
			for node in nodeLst:
				lst.append(node.data)
				nodeLstTmp.append(node)
			nodeLst.clear()
			for node in nodeLstTmp:
				if node.left!=None:
					nodeLst.append(node.left)
				if node.right!=None:
					nodeLst.append(node.right)
			nodeLstTmp.clear()
		return lst

	#节点删除
	def remove(self,data):
		if self.root!=None:
			node = self.root
			if data!=node.data:		#如果不是根节点
				#需要找待删除节点的父节点,是父节点的左子还是右子,待删除节点有左子还是右子
				[parent,pflag,node,cflag]=self.removeFind(data)
				if node!=None:
					self.removeNode(parent,pflag,node,cflag)
			else:
				cflag = self.findChild(node)
				if cflag==0:
					self.root = None
				elif cflag==1:
					self.root = node.left
					node.left = None
				elif cflag==2:
					self.root = node.right
					node.right = None
				elif cflag==3:
					self.removeNode(None,None,node,cflag)
			if node!=None:
				return 1
			else:
				return 0
		else:
			return 0

	#找到待删除节点
	def removeFind(self,data):
		parent = None
		node = self.root
		pflag = 0			#0表待删除节点是父节点的左子，1是右子
		while node!=None:
			if data<node.data:
				parent = node
				pflag = 0
				node = node.left
			elif data>node.data:
				parent = node
				pflag = 1
				node = node.right
			else:
				break
		if node!=None:
			#待删除节点有左子还是右子
			cflag = self.findChild(node)
			return [parent,pflag,node,cflag]
		else:
			return [None,None,None,None]			#没找到

	#查找待删除节点的左右子情况
	def findChild(self,node):
		cflag = 0 			#0表没子，1表有左子，2表有右子，3表有左右子
		if node.left!=None:
			cflag=1
		if node.right!=None:
			if cflag==0:
				cflag = 2
			elif cflag==1:
				cflag = 3
		return cflag

	#执行删除节点方法
	def removeNode(self,parent,pflag,node,cflag):
		if cflag==0:					#是叶子节点
			if pflag==0:
				parent.left=None
			elif pflag==1:
				parent.right=None
		elif cflag==1:					#待删除节点只有左子
			if pflag==0:
				parent.left=node.left
			elif pflag==1:
				parent.right=node.left
			node.left = None	
		elif cflag==2:
			if pflag==0:
				parent.left = node.right
			elif pflag==1:
				parent.right = node.right
			node.right = None
		elif cflag == 3:
			[mparent,mpflag,mnode,mcflag]=self.rightMin(node)
			node.data= mnode.data
			#删除掉右子树中最小节点
			self.removeNode(mparent,mpflag,mnode,mcflag)

	#查找右子树中的最小节点
	def rightMin(self,parent):
		node = parent.right
		pflag = 1
		while node.left!=None:
			parent = node
			pflag = 0
			node = node.left
		cflag = self.findChild(node)
		return [parent,pflag,node,cflag]

# sTree = SortTree()
# lst = [10,6,15,9,3,13,7,16,8]
# for item in lst:
# 	sTree.add(item)
#print(sTree.display())
#print(sTree.preOrder())
#print(sTree.postOrder())
#print(sTree.levelTraverse())
# print(sTree.remove(10))
# print(sTree.remove(3))
# print(sTree.remove(50))
# print(sTree.remove(16))
# print(sTree.display())