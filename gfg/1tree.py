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

	def inorder_tree(self, temp):
		while temp is not None:
			self.inorder_tree(temp.left)
			print(temp.data, end="-")
			self.inorder_tree(temp.right)
			return			
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
print("preorder_tree: ",T.preorder_tree(T.root))
print("postorder_tree: ",T.postorder_tree(T.root))

