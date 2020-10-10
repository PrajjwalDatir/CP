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
		# here zero one and two are to point at the latest 0 1 2 countered so that we can just swap with them
		last_zero = None
		last_one = None
		last_two = None
		temp = None
		current = self.head
		if self.head.data == 1:
			last_one = current
		elif self.head.data == 0:
			last_zero = current
		else:
			last_two = current

		# print(f"current is {current.data}")
		# self.printList()
		current = current.next

		while current.next:

			# print(f"current is {current.next.data}")
			
			if current.next.data == 0:
				print(f"current is {current.next.data}")

				temp = current.next

				if last_zero is None:
					current.next = temp.next
					temp.next = self.head
					self.head = temp
					last_zero = temp
					
					self.printList()
				else:
					current.next = temp.next
					temp.next = last_zero.next
					last_zero.next = temp
					last_zero = temp

					self.printList()
			elif current.next.data == 1:
				
				# print(f"current is {current.next.data}")
				# self.printList()

				temp = current.next

				if last_one is None:


					print(f"current is {current.next.data}")

					self.printList()

					current.next = temp.next

					if last_zero is None:
						temp.next = self.head
						self.head = temp
					else:					
						temp.next = last_zero.next
						last_zero.next = temp
					last_one = temp
					self.printList()
				else:
					current.next = temp.next
					temp.next = last_one.next
					last_one.next = temp
					last_one = temp
			else:
				print(f"current is {current.next.data}")

				self.printList()
				current = current.next
			

ll = linkedList()
# test case : 12012010 answer should be 00011122 

# bug is when we encounter 1 before encountering
ll.push(2)
ll.push(1)
ll.push(0)
# ll.push(1)
# ll.push(0)
# ll.push(2)
# ll.push(0)
# ll.push(1)
# ll.push(0)
ll.printList()
ll.sortList()
ll.printList()