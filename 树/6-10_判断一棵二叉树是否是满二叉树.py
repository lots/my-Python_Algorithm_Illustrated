from 二叉排序树 import SortTree

lst = [20,10,26,5,15,23,28]
sTree = SortTree()
for item in lst:
	sTree.add(item)
lst1 = [sTree.root]
lst2 = []
k = 1
for i in range(sTree.length):
	for node in lst1:
		if node.left!=None:
			lst2.append(node.left)
		if node.right!=None:
			lst2.append(node.right)
	slen = len(lst2)
	if slen==0:
		print("是满二叉树")
		break

	k += 1
	if slen==2**(k-1):
		lst1.clear()
		for node in lst2:
			lst1.append(node)
		lst2.clear()
	else:
		print("不是满二叉树")
		break
