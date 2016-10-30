from random import randint
import datetime

x = []
for num in range(0,100):
	randomNumber = randint(0,10000) 
	x.append(randomNumber)

start = datetime.datetime.now()

for j in range(1,len(x)):
	for i in range(0,j):
		count = 0
		if x[j] < x[i]:
			insertindex = i
			insertvalue = x[j]
			count += 1
			break
	if count > 0:
		del x[j]
		x.insert(insertindex, insertvalue)

print x

end = datetime.datetime.now()
SortTime = end - start
print SortTime



