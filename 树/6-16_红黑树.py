#红黑树节点
class RBTreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None		#左指针
		self.right = None		#右指针
		self.parent = None		#父指针
		self.color = 'black'	#节点颜色默认为黑

class RBTree:
	def __init__(self):
		self.nil = RBTreeNode(0)	#定义空节点
		self.root = self.nil		#根节点默认为空节点

	#插入
	def rbInsert(self,inode):
		pnode = self.nil			#父节点暂定为空节点
		tnode = self.root			#从根节点开始寻找待插入节点位置
		while tnode != self.nil:	#如果搜索到的节点不是空节点
			pnode = tnode			#查找inode对应的父节点
			if inode.data<tnode.data:	#如果inode值小于tnode节点值，向左找
				tnode = tnode.left
			else:					#否则向右找
				tnode = tnode.right
		inode.parent = pnode		#跳出循环后inode的父节点确定为pnode
		if pnode == self.nil:		#如果pnode为空，inode为根节点
			self.root = inode		
		elif inode.data<pnode.data:	#如果inode值小于父节点，inode作为父节点的左子节点
			pnode.left = inode
		else:						#否则就是右子节点
			pnode.right = inode
		inode.left = self.nil		#给inode节点加两个空的叶子节点
		inode.right = self.nil		#新加入的inode默认为红色
		inode.color = 'red'
		#上色和旋转处理
		self.rbInsertFixup(inode)	#对新加入的inode节点做上色和旋转处理
		return inode.data
	#左旋
	def leftRotate(self,node):
		rNode = node.right    			#拿到当前节点的右子节点指针
		node.right = rNode.left     	#当前节点的右指针指向右子节点的左子节点
		if rNode.left != self.nil:		#如果右子节点的左子节点不是空
			rNode.left.parent = node    #右子节点的左子节点的父节点指针指向当前节点
		rNode.parent = node.parent      #右子节点的父节点指针指向当前节点的父节点
		if node.parent == self.nil:     #如果当前节点的父节点是空节点
			self.root = rNode           #根节点指向当前节点的右子节点
		elif node == node.parent.left:  #如果当前节点是父节点的左子节点
			node.parent.left = rNode    #当前节点的父节点的左指针指向右子节点
		else:							#如果当前节点是父节点的右子节点
			node.parent.right = rNode   #当前节点的父节点的右指针指向右子节点
		rNode.left = node               #右子节点的左指针指向当前节点
		node.parent = rNode             #当前节点的父节点指针指向原先的右子节点
	#右旋
	def rightRotate(self,node):
		lNode = node.left               #拿到当前节点的左子节点
		node.left = lNode.right         #当前节点的左指针指向左子节点的右子节点
		if lNode.right != self.nil:     #如果左子节点的右子节点不是空节点
			lNode.right.parent = node   #左子节点的右子节点的父节点指针指向当前节点
		lNode.parent = node.parent      #左子节点的父节点指针指向当前节点的父节点
		if node.parent==self.nil:       #如果当前节点的父节点为空节点
			self.root = lNode           #根节点指向左子节点
		elif node == node.parent.right: #如果当前节点是父节点的右子节点
			node.parent.right = lNode   #当前节点的父节点的右指针指向左子节点
		else:                           #否则就是父节点的左子节点
			node.parent.left = lNode    #当前节点的父节点的左指针指向左子节点
		lNode.right = node              #左子节点的右指针指向当前节点
		node.parent = lNode             #当前节点的父节点指针指向左子节点

	def rbInsertFixup(self,cnode):
		while cnode.parent.color=='red':				#当前节点的父节点的颜色是红色，进入循环
			if cnode.parent==cnode.parent.parent.left:  #如果当前节点的父节点是爷爷节点的左子节点
				layerNode = cnode.parent.parent.right   #拿到爷爷节点的右子节点(叔叔节点)
				if layerNode.color=='red':              #如果爷爷节点的右子节点颜色是红色的
					cnode.parent.color='black'          #当前节点的父节点变黑
					layerNode.color='black'             #当前节点的叔叔节点也变黑
					cnode.parent.parent.color='red'		#当前节点的爷爷节点变红
					cnode = cnode.parent.parent			#当前节点变成爷爷节点
				else:			#爷爷节点的另一节点为黑
					if cnode==cnode.parent.right:       #如果当前节点是父节点的右子节点
						cnode = cnode.parent            #当前节点转为当前节点的父节点
						self.leftRotate(cnode)			#在当前节点上做左旋方法
					cnode.parent.color = 'black'        #当前节点的父节点颜色变黑
					cnode.parent.parent.color = 'red'	#当前节点的爷爷节点颜色变红
					self.rightRotate(cnode.parent.parent) #调用右旋方法旋转爷爷节点

			else:									#如果当前节点的父节点是爷爷节点的右子节点
				layerNode = cnode.parent.parent.left #拿到爷爷节点的左子节点(叔叔节点)
				if layerNode.color == 'red':		#如果叔叔节点的颜色是红色
					cnode.parent.color='black'      #当前节点的父节点的颜色变成黑色
					layerNode.color='black'			#叔叔节点颜色变黑
					cnode.parent.parent.color='red' #当前节点的爷爷节点的颜色变红
					cnode = cnode.parent.parent     #当前节点指针转为爷爷节点
				else:								#如果叔叔节点的颜色是黑色
					if cnode == cnode.parent.left:  #如果当前节点的父节点的左子节点
						cnode = cnode.parent        #当前节点转为当前节点的父节点
						self.rightRotate(self,cnode)#在当前节点上做右旋操作
					cnode.parent.color='black'      #当前节点的父节点颜色变黑
					cnode.parent.parent.color='red' #当前节点的爷爷节点颜色变红
					self.leftRotate(self,cnode.parent.parent) #对爷爷节点做左旋操作
		self.root.color = 'black'					#根节点变成黑色

	#中序遍历
	def midSort(self,node):
		if node!=None:						#如果当前节点不为空
			self.midSort(node.left)			#递归调用当前节点的左子节点
			if node.data!=0:				#如果当前节点值不为0
				print('data:',node.data,'node.parent:',node.parent.data)
			self.midSort(node.right)		#递归调用当前节点的右子节点

nodes = [11,2,14,1,7,15,5,8,4]
rbTree = RBTree()
for node in nodes:
	print("插入数据:",rbTree.rbInsert(RBTreeNode(node)))

print("插入完成，中序遍历")
rbTree.midSort(rbTree.root)