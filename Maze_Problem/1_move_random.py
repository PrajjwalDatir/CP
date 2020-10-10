from tkinter import Tk, Canvas
import random
import time

DIR_RIGHT = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_UP = 3

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

def get_mazetrix():
    with open("mazetrix.txt") as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines]


def get_mouse_xy():
    for y, row in enumerate(mazetrix):
        x = row.find("M")
        if(x != -1):
            return x, y


def draw_maze():
    for y, row in enumerate(mazetrix):
        for x, ch in enumerate(row):
            if(is_wall(x, y)):
                draw_wall(x, y)


def draw_wall(x, y):
    draw(x, y, "green")

def draw_mouse(x, y):
    draw(x, y, "red")

def draw_footprint(x, y):
    draw(x, y, "yellow")


def draw(x, y, color):

    maze_height = len(mazetrix)
    maze_width = len(mazetrix[0])
    height = canvas_height/maze_height
    width = canvas_width/maze_width

    x1, y1 = (x*width, y*height)
    x2, y2 = (x1+width, y1+height)
    w.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


def is_wall(x, y):
    return mazetrix[y][x] == '#'

def is_exit(x, y):
    return mazetrix[y][x] == 'E'


random.seed(18)
canvas_height = 450
canvas_width = 750

def main():
    global root, w, mazetrix, x, y
    mazetrix = get_mazetrix()
    x, y = get_mouse_xy()
    root = Tk()
    root.title("Mouse in a Maze")
    w = Canvas(root, bg="white", width=canvas_width, height=canvas_height)
    w.pack()
    draw_maze()
    move_the_mouse()
    root.mainloop()



steps = 0

def move_the_mouse():

    global x, y, steps

    while True:

        new_y, new_x = x, y
        new_direction = get_good_move(new_y,new_x)
        new_direction = get_next_move_random()
        print("{", new_y, new_x, "}")
        if(new_direction == DIR_RIGHT):
            new_y += 1
        if(new_direction == DIR_DOWN):
            new_x += 1
        if(new_direction == DIR_LEFT):
            new_y -= 1
        if(new_direction == DIR_UP):
            new_x -= 1

        if(not is_wall(new_y, new_x)):
            break

    # time.sleep(1)

    draw_footprint(x, y)
    x, y = new_y, new_x
    draw_mouse(x, y)

    steps += 1

    if(is_exit(x, y)):
        print("Total steps: " + str(steps))
    else:
        root.after(10, move_the_mouse)



def get_next_move_random():    
    dirs = [DIR_RIGHT, DIR_DOWN, DIR_LEFT, DIR_UP]
    return dirs[random.randint(0, len(dirs)-1)]

def get_good_move(mou_y, mou_x):
	s = stack()
	visited = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    # if(not is_wall(new_y, new_x)):
	available_options = [DIR_RIGHT, DIR_DOWN, DIR_LEFT, DIR_UP]
	
	 # right  y,x+1
	if mou_x == 13:
		available_options.remove(DIR_RIGHT)
	elif (is_wall([mou_x][mou_y + 1]) or visited[mou_y][mou_x + 1] == 1):
		available_options.remove(DIR_RIGHT)
	 # down y+1, x
	if mou_y == 23:
		available_options.remove(DIR_DOWN)
	elif (is_wall([mou_y + 1][mou_x]) or visited[mou_y + 1][mou_x] == 1):
		available_options.remove(DIR_DOWN)
	 # up y-1 , x
	if mou_y == 1:
		available_options.remove(DIR_UP)
	elif(is_wall([mou_y - 1][mou_x]) or visited[mou_y - 1][mou_x] == 1):
		available_options.remove(DIR_UP)
	 # left y, x-1
	if mou_x == 1:
		available_options.remove(DIR_LEFT)
	elif(is_wall([mou_y][mou_x - 1]) or visited[mou_y][mou_x - 1] == 1):
		available_options.remove(DIR_LEFT)

	if len(available_options) == 0:
		if s.is_empty():
			print("No soln")
			return 0
		else:
			temp = s.pop()
			print("temp",temp)
			mou_y, mou_x = s.peek()

	s.push([mou_y,mou_x])
	visited[mou_y][mou_x] = 1


	return available_options[0]


main()
