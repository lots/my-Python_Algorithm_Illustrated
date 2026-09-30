from 单向链表 import SlinkedList

a = SlinkedList()
b = SlinkedList()
a.append(2)				#分别向两个链表中添加元素
a.append(3)
a.append(8)
a.append(11)
a.append(13)
a.append(17)
b.append(3)
b.append(5)
b.append(9)
b.append(12)
c = SlinkedList()
pa = a.phead
pb = b.phead
while pa!=None and pb!=None:
	if pa.data<pb.data:
		c.append(pa.data)
		pa = pa.next
	else:
		c.append(pb.data)
		pb = pb.next
while pa!=None:
	c.append(pa.data)
	pa = pa.next
while pb!=None:
	c.append(pb.data)
	pb = pb.next

print(c.display())