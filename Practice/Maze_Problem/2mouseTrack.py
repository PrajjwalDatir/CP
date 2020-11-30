# 2mouseTrack.py
import time
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
			return
		return self.top.data

	def print_stack(self):
		if self.top is None:
			print()
			return
		temp = self.top
		while temp.next:
			print(temp.data)
			temp = temp.next
		print(temp.data)
		return

	def is_empty(self):
		if self.top is None:
			return True

def print_matrix(mat):
	for i in range(5):
		print(mat[i])
	print()
	
def solve(start, end , mat):
	visited = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],]

	# print_matrix(visited)
	
	s = stack()
	mou_y = start[0]
	mou_x = start[1]
	s.push([mou_y,mou_x])
	visited[mou_y][mou_x] = 1
	# available options are 				right = 0, down = 1, up = 2, left = 3
	while (mou_y != end[0]) or (mou_x != end[1]):
		available_options = [0, 1, 2, 3]
	 # right  y,x+1
		if mou_x == 4:
			available_options.remove(0)
		elif (mat[mou_y][mou_x + 1] == 1 or visited[mou_y][mou_x + 1] == 1):
			available_options.remove(0)
	 # down y+1, x
		if mou_y >= 4:
			available_options.remove(1)
		elif (mat[mou_y + 1][mou_x] == 1 or visited[mou_y + 1][mou_x] == 1):
			available_options.remove(1)
	 # up y-1 , x
		if mou_y == 0:
			available_options.remove(2)
		elif(mat[mou_y - 1][mou_x] == 1 or visited[mou_y - 1][mou_x] == 1):
			available_options.remove(2)
	 # left y, x-1
		if mou_x == 0:
			available_options.remove(3)
		elif(mat[mou_y][mou_x - 1] == 1 or visited[mou_y][mou_x - 1] == 1):
			available_options.remove(3)			

		time.sleep(1)
		print("available_options",available_options)
		if len(available_options) == 0:
			if s.is_empty():
				print("No soln")
				return 0
			else:
				temp = s.pop()
				print("temp",temp)
				mou_y, mou_x = s.peek()
		else:
			# last_option = available_options[0]
			s.push([mou_y,mou_x])
			if available_options[0] == 0: # right
				mou_x += 1
			elif available_options[0] == 1: # down
				mou_y += 1
			elif available_options[0] == 2: # up
				mou_y -= 1
			elif available_options[0] == 3: # left
				mou_x -= 1
			visited[mou_y][mou_x] = 1
	
		print("[ ", mou_y,", ", mou_x, " ]")
		# print("visitedmatrix:")
		# print_matrix(visited)
		available_options = [0, 1, 2, 3]

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
	print_matrix(mat)
	solve(start,end, mat)


if __name__ == '__main__':
	main()