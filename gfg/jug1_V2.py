# jug1_V2.py
# Question 1
"""
so we have linked list with data only equal to 0 , 1 or 2 and we have to sort them in O(n) as I think before prajjwal knows the answer of this question
"""

#so first we need linked list to start withs
class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	"""docstring for linkedList"""
	def __init__(self):
		self.head = None

	def push(self, data):
		temp = self.head
		newnode = Node(data)
		if self.head is None:
			self.head = newnode
			return
		else:
			while temp.next is not None:
				temp = temp.next
			temp.next = newnode

	def printList(self):
		temp = self.head
		if self.head is None:
			print("List is empty")
			return 0
		while temp.next:
			print(temp.data, end="->")
			temp = temp.next
		print(temp.data)
		return 1

	def sortList(self):
		if self.head is None:
			print("Nothing to sort here.")
			return
		elif self.head.next is None:
			return
		
		last_zero = None
		last_one = None
		last_two = None

		current = self.head

		# part 0th of process
		while current:
			if current.data == 0:
				if last_zero is None:
					last_zero = current
					# print(current.data, end="None\n")
					current = current.next
					last_zero.next = None
				else:
					temp = current.next
					if last_zero.next is not None:
						current.next = last_zero.next
						last_zero.next = current
					else:
						last_zero.next = current
						current.next = None
					# print(current.data)
					current = temp
					# advanced

			elif current.data == 1:
				if last_one is None:
					last_one = current
					# print(current.data, end="None\n")
					current = current.next
					last_one.next = None

				else:
					temp = current.next
					if last_one.next is not None:
						current.next = last_one.next
						last_one.next = current
					else:
						last_one.next = current
						current.next = None
					
					# print(current.data)
					current = temp
					# advanced

			elif current.data == 2:
				if last_two is None:
					last_two = current
					# print(current.data, end="None\n")
					current = current.next
					last_two.next = None
					
				else:
					temp = current.next
					if last_two.next is not None:
						current.next = last_two.next
						last_two.next = current
					else:
						last_two.next = current
						current.next = None
					
					# print(current.data)
					current = temp
					# advanced
			else:
				print("Given linkedList is not Ideal")
				return 1

		#part 2
		def noUse():
			temp = last_zero
			while temp:
				print(temp.data, end="->")
				temp = temp.next

			print()
			temp = last_one
			while temp:
				print(temp.data, end="->")
				temp = temp.next
			print()
			temp = last_two
			while temp:
				print(temp.data, end="->")
				temp = temp.next
			print()

		# noUse()
		if last_zero:
			self.head = last_zero
			temp = last_zero
			while temp.next:
				# print(temp.data)
				temp = temp.next
			if last_one:
				temp.next = last_one
				while temp.next:
					# print(temp.data)
					temp = temp.next
			temp.next = last_two

		elif last_one:
			self.head = last_one
			temp = last_one
			while temp.next:
				temp = temp.next
			temp.next = last_two

		else:
			self.head = last_two



ll = linkedList()
# test case : 12012010 answer should be 00011122 

ll.push(2)
ll.push(0)
ll.push(1)
ll.push(2)
ll.push(1)
ll.push(2)
ll.push(0)
ll.push(1)
ll.push(0)
ll.printList()
ll.sortList()
ll.printList()