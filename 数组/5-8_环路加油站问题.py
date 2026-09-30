gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
glen = len(gas)
diff = []
for i in range(glen):
	diff.append(gas[i]-cost[i])

start = 0
sum = 0				#差值和

for i in range(start,glen):
	sum += diff[i]
	if sum<0:
		start = i+1
		sum = 0

for i in range(0,start):
	sum += diff[i]
	if sum<0:
		break

if sum>=0:
	print("转完全程的起点在:",start)
else:
	print("所给油量转不完全程")
