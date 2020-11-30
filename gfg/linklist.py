class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		#will be of type Node

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

	def printList(self):
		if self.head is None:
			print("List is empty")
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def deleteNode(self, key):
		temp = self.head

		if temp.data == key:
			self.head = temp.next
			temp = None

		while temp is not None:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return
		prev.next = temp.next
		temp.next = None

if __name__ == '__main__':
	ll = LinkedList()
	ll.append('append1')
	ll.push('pushed1')
	ll.append('append2')
	ll.insertAfter(ll.head.next, 'insertAfter')
	print('LinkedList is :')
	ll.printList()
	ll.deleteNode('append1')
	print('LinkedList is :')
	ll.printList()