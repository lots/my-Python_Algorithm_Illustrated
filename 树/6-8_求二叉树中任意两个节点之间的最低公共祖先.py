from 二叉排序树 import SortTree
sTree = SortTree()
lst = [10,6,15,9,3,13,7,16,8,2,5,4,14,16,19]
for item in lst:
	sTree.add(item)

def lookup(v,lst):
	global sTree
	node = sTree.root
	slen = sTree.length
	for i in range(slen):
		lst.append(node)
		if v<node.data:
			if node.left!=None:
				node = node.left
			else:
				return None
		elif v>node.data:
			if node.right!=None:
				node = node.right
			else:
				return None
		else:
			return lst

v1 = 4
v2 = 8
lst1 = []
lst2 = []
lookup(v1,lst1)
lookup(v2,lst2)
slen = len(lst1)
commonNode = None
for i in range(slen):
	p1 = lst1[i]
	p2 = lst2[i]
	if p2!=None and p1!=p2:
		break
	commonNode = p1

if commonNode!=None:
	print("最低公共祖先:",commonNode.data)