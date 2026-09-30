from 单向链表 import SlinkedList

slinkList = SlinkedList()
for i in range(10):
	slinkList.append(i)

lst = slinkList.display()
print(lst)

slinkList.rev()
lst = slinkList.display()
print(lst)

slinkList.rev()
lst = slinkList.display()
print(lst)