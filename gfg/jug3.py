# jug3.py
T = int(input())
repeat = 0
while T:
	n = int(input())
	A = list(map(int , input().split(" ")))
	# write 
	maxi = 0
	ans = None

	for i in range(n):
		if A[i] is None:
			continue
		previous = False
		current = A[i]
		repeat = 0

		for j in range(n):
			if A[j] == current and not previous:
				previous = True
				A[j] = None
				repeat += 1
			else:
				previous = False
		if repeat > maxi:
			ans = current
			maxi = repeat
		elif repeat == maxi:
			if (ans is None) or (current < ans) :
				ans = current
	print(ans)
	T -= 1 