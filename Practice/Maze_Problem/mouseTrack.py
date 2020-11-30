class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class stack:
	"""docstring for stack"""
	def __init__(self):
		self.top = None
		
	def push(self, data):
		newnode = node(data)
		if self.top is None:
			self.top = newnode
			return
		newnode.next = self.top
		self.top = newnode

	def pop(self):
		if self.top is None:
			print("Stack is empty")
		temp = self.top.data
		self.top = self.top.next
		return temp

	def peek(self):
		if self.top is None:
			print("Stack is empty")
		return self.top.data

	def print_stack(self):
		temp = self.top
		while temp.next:
			print(temp.data, end="->")
			temp = temp.next
		print(temp.data)
		return

	def is_empty(self):
		if self.top is None:
			return True

def solve(start, end, mat):
	s = stack()
	mou_x = start[0]
	mou_y = start[1]
	# available options are 				right = 0, down = 1, up = 2, left = 3
	while (mou_x != end[0]) or (mou_y != end[1]):
		# print("[ ", mou_x,", ", mou_y, " ]")
		available_options = [0, 1, 2, 3]
		if not s.is_empty():
			# print(s.top.data)
			available_options.remove(abs(s.top.data - 3))
		# print(available_options)
		for opt in available_options:
			if opt == 0: # right  x,y+1
				if mou_y == 4:
					available_options.remove(opt)
				elif (mat[mou_x][mou_y + 1] == 1) :
					available_options.remove(opt)
			elif opt == 1: # down x+1, y
				if mou_x >= 4:
					available_options.remove(opt)
				elif (mat[mou_x + 1][mou_y] == 1):
					available_options.remove(opt)
			elif opt == 2: # up x-1 , y
				if mou_x == 0:
					available_options.remove(opt)
				elif(mat[mou_x - 1][mou_y] == 1):
					available_options.remove(opt)
			elif opt == 3: # left x, y-1
				if mou_y == 0:
					available_options.remove(opt)
				elif(mat[mou_x][mou_y - 1] == 1):
					available_options.remove(opt)			

		if not len(available_options):
			if s.is_empty():
				print("No soln")
				return 0
			else:
				temp = s.pop()
				if temp == 0: # right
					mou_y -= 1
				elif temp == 1: # down
					mou_x -= 1
				elif temp == 2: # up
					mou_x += 1
				elif temp == 3: # left
					mou_y += 1

		else:
			print("[ ", mou_x,", ", mou_y, " ]")
			s.push(available_options[0])
			if available_options[0] == 0: # right
				mou_y += 1
			elif available_options[0] == 1: # down
				mou_x += 1
			elif available_options[0] == 2: # up
				mou_x -= 1
			elif available_options[0] == 3: # left
				mou_y -= 1

		if mou_x == start[0] and mou_y == start[1]:
			print("No soln")
			return 0
	print("[ ", mou_x,", ", mou_y, " ]")
	print("soln:")
	s.print_stack()
	return 1


def main():
	mat =  [[0, 0, 0, 0, 1],
			[0, 1, 1, 1, 0],
			[0, 1, 0, 0, 0],
			[0, 1, 0, 1, 0],
			[0, 0, 0, 1, 0]]
	start = [0,0]
	end = [4,4]
	print(mat[0])
	print(mat[1])
	print(mat[2])
	print(mat[3])
	print(mat[4])
	print()
	solve(start,end, mat)


if __name__ == '__main__':
	main()