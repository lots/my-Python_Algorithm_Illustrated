from 二叉排序树 import SortTree
sTree = SortTree()
lst = [10,6,15,9,3,13,7,16,8]
for item in lst:
	sTree.add(item)

root = sTree.root
lst1 = [root]
lst2 = []
minLayer = 0
maxLayer = 0
k = 1
for i in range(sTree.length):
	flag = 0					#判断节点是否有后,0无后，1有后
	for node in lst1:
		if node.left!=None:
			flag=1
			lst2.append(node.left)
		if node.right!=None:
			flag=1
			lst2.append(node.right)
		if minLayer==0 and flag==0:
			minLayer = k
	if len(lst2)==0:
		maxLayer = k
		break
	k = k+1
	lst1.clear()
	for node in lst2:
		lst1.append(node)
	lst2.clear()

print("最小深度:",minLayer)
print("最大深度:",maxLayer)