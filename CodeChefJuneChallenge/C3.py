
#C3.py
import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	fives = 0
	tens = 0
	bankrupt = False
	total = int(sys.stdin.readline())
	cus_queue = list(sys.stdin.readline().split())
	#print(cus_queue)
	for i in range(total):
		#print(bank)
		current = int(cus_queue[i])
		if current == 5:
			fives += 1
		elif current == 10:
			if fives <= 0:
				bankrupt = True
			fives -= 1
			tens += 1
		elif current == 15:
			if tens > 0:
				tens -= 1
			elif fives >= 2:
				fives -= 2
			#else if (tens <= 0) and (fives < 2):
			else:
				bankrupt = True 
			
		if bankrupt:
			print("NO")
			break

	if not bankrupt:
		print("YES")
