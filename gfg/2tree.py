# the problem was ki two nodes are wrong so swap them
import time
class node:
	"""docstring for node"""
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class TreeDS:
	"""docstring for TreeDS"""
	def __init__(self):
		self.root = None
	def is_empty(self):
		return self.root is None
	
	def search(self, thisdata):
		print("Traversing")
		if self.root:
			temp = self.root
			while not temp.data == thisdata:
				print(temp.data)
				if thisdata < temp.data:
					temp = temp.left
				elif thisdata > temp.data:	
					temp = temp.right
				if temp is None:
					print("not found")
					return
			print(temp.data)
			print("found it")
			return

	def inorder_tree(self, temp, s=None):
		if s is None:
			s = []
		while temp is not None:
			self.inorder_tree(temp.left, s)
			# print(temp.data, end="-")
			s.append(temp.data)
			self.inorder_tree(temp.right, s)
			return s
	def preorder_tree(self, temp):
		while temp:
			print(temp.data, end="-")
			self.preorder_tree(temp.left)
			self.preorder_tree(temp.right)
			return
			
	def postorder_tree(self, temp):
		while temp:
			self.postorder_tree(temp.left)
			self.postorder_tree(temp.right)
			print(temp.data, end="-")			
			return
	def push(self, data):
		newnode = node(data)
		if self.is_empty():
			self.root = newnode
			return
		temp = self.root
		while True:
			if newnode.data < temp.data:
				if temp.left is None:
					temp.left = newnode
					return
				temp = temp.left
			if newnode.data > temp.data:
				if temp.right is None:
					temp.right = newnode
					return
				temp = temp.right

	def findwrong(self, temp):
		
		s = self.inorder_tree(self.root)
		# print(s)
		temp = []
		for i in range(len(s) - 1):
			if s[i] > s[i+1]:
				if not len(temp):
					# print(s[i])
					temp.append(s[i])
				else:
					# print(s[i+1])
					temp.append(s[i+1])
		print(temp)
		self.replacewrong(self.root, temp)
		return

	def replacewrong(self, temp, thisdata):
		# print("replacing: ")
		count = 0
		swap1 = None
		swap2 = None

		while count != 2:
			temp = self.root
			while not temp.data == thisdata[count]:
				# print(temp.data)
				if thisdata[abs(count - 1)] < temp.data:
					temp = temp.left
				elif thisdata[abs(count - 1)] > temp.data:
					temp = temp.right
				if temp is None:
					print("not found")
					return
			# print(temp.data, "replaced by: ", rep)
			# temp.data = rep
			if swap1:
				swap2 = temp
			else:
				swap1 = temp

			count += 1
		swap1.data , swap2.data = swap2.data, swap1.data
		return self.root

		
	def replace(self, temp, thisdata):
		print("replacing: ", thisdata)
		count = 0
		swap1 = None
		swap2 = None

		while count != 2:
			temp = self.root
			while not temp.data == thisdata[count]:
				# print(temp.data)
				if thisdata[count] < temp.data:
					temp = temp.left
				elif thisdata[count] > temp.data:
					temp = temp.right
				if temp is None:
					print("not found")
					return
			# print(temp.data, "replaced by: ", rep)
			# temp.data = rep
			if swap1:
				swap2 = temp
			else:
				swap1 = temp

			count += 1
		swap1.data , swap2.data = swap2.data, swap1.data
		return self.root
				
T = TreeDS()
T.push(5)
T.push(3)
T.push(4)
T.push(1)
T.push(7)
T.push(6)
# T.search(5)
# T.search(3)
# T.search(10)

print("inorder_tree: ", T.inorder_tree(T.root))
T.replace(T.root, [4,6])
print("inorder_tree: ", T.inorder_tree(T.root))
T.findwrong(T.root)
print("inorder_tree: ", T.inorder_tree(T.root))

# print("inorder_tree: ", T.inorder_tree(T.root))
# print("preorder_tree: ",T.preorder_tree(T.root))
# print("postorder_tree: ",T.postorder_tree(T.root))

