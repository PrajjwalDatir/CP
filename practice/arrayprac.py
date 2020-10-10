import array

arr = array.array('h', [])

for i in range(0,10):
	arr.append(i)
print(arr)
arr.insert(5, 7)
print(arr)