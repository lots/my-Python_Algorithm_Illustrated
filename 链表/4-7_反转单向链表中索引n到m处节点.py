from 单向链表 import SlinkedList
sLinkedList = SlinkedList()
for i in range(10):
	sLinkedList.append(i)

lst = sLinkedList.display()
print(lst)

sLinkedList.passrev(3,7)
lst = sLinkedList.display()
print(lst)