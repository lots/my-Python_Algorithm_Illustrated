class BNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.bfactor = 0	#左侧节点数-右侧节点数

class BalanceTree:
	def __init__(self):
		self.root = None
		self.length = 0

	def add(self,data):
		if self.root !=None:
			self.addData(self.root,data)
		else:
			node = BNode(data)
			self.root = node

		self.length += 1

	def addData(self,node,data):
		if node.bfactor == 0:		#==0,左侧等于右侧
			if data<node.data:
				node.bfactor += 1
				if node.left!=None:
					self.addData(node.left,data)
				else:
					node.left = BNode(data)
			else:
				node.bfactor -= 1
				if node.right!=None:
					self.addData(node.right,data)
				else:
					node.right = BNode(data)

		elif node.bfactor>0:		#==1,左侧比右侧多1个节点 
			node.bfactor -= 1
			if data<node.data:
				if node.right!=None:
					self.addData(node.right,node.data)
				else:
					node.right = BNode(node.data)
				#用data和左侧最大值中更大的数值替换本节点
				self.leftThanRight(node,data)
			else:
				if node.right!=None:
					self.addData(node.right,data)
				else:
					node.right = BNode(data)
		else:						#==-1,左侧比右侧少1个节点
			node.bfactor += 1
			if data<node.data:
				if node.left!=None:
					self.addData(node.left,data)
				else:
					node.left = BNode(data)
			else:
				if node.left!=None:
					self.addData(node.left,node.data)
				else:
					node.left = BNode(node.data)
				#用data和左侧最大值中更大的数值替换本节点
				self.rightThanLeft(node,data)


	def leftThanRight(self,node,data):
		#查找左侧最大值节点
		[pNode,pflag,lmNode,path] = self.leftMaxNode(node)
		if lmNode.data>data:
			node.data = lmNode.data
			if pflag==1:
				pNode.right = None
			else:
				pNode.left = None
			del lmNode
			node.bfactor -= 1
			for ppNode in path:
				ppNode.bfactor += 1
			self.addData(node,data)
		else:
			node.data = data

	def rightThanLeft(self,node,data):
		#查找左侧最大值节点
		[pNode,pflag,rmNode,path] = self.rightMinNode(node)
		if rmNode.data<data:
			node.data = rmNode.data
			if pflag==0:
				pNode.left = None
			else:
				pNode.right = None
			del rmNode
			node.bfactor += 1
			for ppNode in path:
				ppNode.bfactor -= 1
			self.addData(node,data)
		else:
			node.data = data

	def leftMaxNode(self,node):
		pNode = node
		lmNode = node.left
		pflag = 0
		path = []			#查找路径
		while lmNode.right!=None:
			pflag=1
			pNode = lmNode
			path.append(pNode)
			lmNode = lmNode.right
		return [pNode,pflag,lmNode,path]

	def rightMinNode(self,node):
		pNode = node
		rmNode = node.right
		pflag = 1
		path = []			#查找路径
		while rmNode.left!=None:
			pflag=0
			pNode = rmNode
			path.append(pNode)
			rmNode = rmNode.left
		return [pNode,pflag,rmNode,path]

	def remove(self,data):
		if self.root!=None:
			path = [self.root]
			self.removeData(path,data)
		else:
			return None

	def removeData(self,path,data):
		node = path[-1]
		if data<node.data:
			if node.left!=None:
				path.append(-1)
				path.append(node.left)
				return self.removeData(path,data)
			else:
				return None
		elif data>node.data:
			if node.right!=None:
				path.append(1)
				path.append(node.right)
				return self.removeData(path,data)
			else:
				return None
		else:
			#如果只有左子树,直接用左子节点替换删除节点
			if(node.left!=None and node.right==None):
				pnode = path[-3]
				direction = path[-2]
				lnode = node.left
				if direction == -1:
					pnode.left = lnode
				else:
					pnode.right = lnode
				node.left = None

			#如果只有右子树,直接用右子节点替换删除节点
			elif(node.left==None and node.right!=None):
				pnode = path[-3]
				direction = path[-2]
				rnode = node.right
				if direction == -1:
					pnode.left = rnode
				else:
					pnode.right = rnode
				node.right = None
			#如果没有左右子树,直接删除
			elif(node.left==None and node.right==None):
				pnode = path[-3]
				direction = path[-2]
				if direction == -1:
					pnode.left = None
				else:
					pnode.right = None
			#如果同时有左右子树,用右侧最小值替换删除节点，删除右侧最小节点，平衡因子-1
			else:
				#找到右子树中的最小值
				[rpNode,rpflag,rmNode,rpath] = self.rightMinNode(node)
				#替换掉待删除节点中的data
				node.data = rmNode.data
				#删除右侧最小值节点
				if rpflag==0:
					rpNode.left = None
				else:
					rpNode.right = None
				del rmNode
				node.bfactor += 1
				for ppNode in rpath:
					ppNode.bfactor += 1

			#遍历path路径，凡是失衡节点再做纠偏
			pathLen = len(path)-1
			delpath = []
			for i in range(0,pathLen,2):
				dpnode = path[i]
				dpnode.bfactor += path[i+1]
				delpath.append(dpnode)
			while len(delpath)>0:
				pathNode = delpath.pop()
				if abs(pathNode.bfactor)>1:
					#纠偏
					self.correct(pathNode)

	def correct(self,node):
		if node.bfactor>1:
			#node.data向右插入
			if node.right!=None:
				self.addData(node.right,node.data)
			else:
				node.right = BNode(node.data)
			node.bfactor -= 1
			#取左侧最大值替换node.data
			[pNode,pflag,lmNode,path]=self.leftMaxNode(node)
			node.data = lmNode.data
			#删除左侧最大值节点
			if pflag==1:
				pNode.right=None
			else:
				pNode.left=None
			del lmNode
			node.bfactor -= 1
			for ppNode in path:
				ppNode.bfactor += 1
		else:
			#node.data向左插入
			if node.left!=None:
				self.addData(node.left,node.data)
			else:
				node.left = BNode(node.data)
			node.bfactor += 1
			#取左侧最大值替换node.data
			[pNode,pflag,rmNode,path]=self.rightMinNode(node)
			node.data = rmNode.data
			#删除左侧最大值节点
			if pflag==1:
				pNode.right=None
			else:
				pNode.left=None
			del rmNode
			node.bfactor += 1
			for ppNode in path:
				ppNode.bfactor -= 1

			while len(path)>0:
				pathNode = path.pop()
				if abs(pathNode.bfactor)>1:
					self.correct(pathNode)

#lst = [2,1,4,3,5,6]
lst = [2,1,4,3,5,6,11,9]
bTree = BalanceTree()
for item in lst:
	bTree.add(item)

print(bTree.root.data)

bTree.remove(2)

lst1 = []
def display(node,lst):
	if node.left!=None:
		display(node.left,lst)
	lst.append(node.data)
	if node.right!=None:
		display(node.right,lst)
display(bTree.root,lst1)
print('平衡二叉树的排序输出:',lst1)

print("分层打印")
lst1 = [bTree.root]
lst2 = []
flag = 1

while flag==1:
	flag = 0
	for item in lst1:
		if item!=None:
			lst2.append(item.left)
			lst2.append(item.right)
			flag=1
		else:
			lst2.append(None)
			lst2.append(None)

	for item in lst1:
		if item!=None:
			print(item.data,end='')
			print('(',item.bfactor,')',end=',')
		else:
			print(None,end=',')
	print('')
	lst1.clear()
	for item in lst2:
		lst1.append(item)
	lst2.clear()



