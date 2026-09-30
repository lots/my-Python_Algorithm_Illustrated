from 二叉排序树 import SortTree
lst = [20,10,26,5,15,28,3,7,17,21]
sTree = SortTree()
for item in lst:
	sTree.add(item)

lst1 = [sTree.root]
lst2 = []
k = 1
for i in range(sTree.length):
	sflag = 0
	nflag = 0
	for node in lst1:
		if node.left!=None:
			if sflag==0:
				lst2.append(node.left)
			else:
				nflag=1
		else:
			sflag=1
		if node.right!=None:
			if sflag==0:
				lst2.append(node.right)
			else:
				nflag=1
		else:
			sflag=1
	if nflag==1:
		print("此树不是完全二叉树")
		break
	slen = len(lst2)
	if slen==0:
		print("此树是完全二叉树")
		break

	lst1.clear()
	for node in lst2:
		lst1.append(node)
	lst2.clear()

