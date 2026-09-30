from 单向链表 import SlinkedList

def revprint(node):
	if node.next!=None:
		revprint(node.next)
	print(node.data)

linkedList = SlinkedList()
for i in range(10):
	linkedList.append(i)

node = linkedList.phead
revprint(node)