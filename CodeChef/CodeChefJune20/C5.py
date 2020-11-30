

import sys
"""
for 3
1 2 3
4 5 6
7 8 9
for 4
1  2  3  4
8  7  6  5
9  10 11 12
16 15 14 13
"""
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	N = int(sys.stdin.readline())
	if N % 2:
		for parent in range(N):
			for child in range(1, N + 1):
				if child < N:
					print(parent * N + child,end=" ")
				else:
					print(parent * N + child)
	else:
		for parent in range(N):
			#print(parent)
			if not parent % 2:
				for child in range(1, N + 1):
					if child < N:
						print(parent * N + child,end=" ")
					else:
						print(parent * N + child)	
			else:
				for child in range(N):
					if child < N - 1:
						print((parent+1) * N - child,end=" ")
					else:
						print((parent+1) * N - child)	
					