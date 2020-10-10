
#C2.py
import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	pair = 0
	mode = 0
	stud_queue = list(sys.stdin.readline())	
	#print(len(stud_queue))
	#print(stud_queue)
	if len(stud_queue) <= 2:
		print("0")
		continue
	for num in range(len(stud_queue) - 2):
		current = stud_queue[num]
		front = stud_queue[num + 1]
		#print(num)
		#print(current)
		#print(front)
		if mode == 1:
			mode = 0
			continue
		elif (current != front):
			pair = pair + 1
			mode = 1
		#print(stud_queue)
	print(pair)