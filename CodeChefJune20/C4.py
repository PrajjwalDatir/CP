

import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	TS = int(sys.stdin.readline())
	mul = 2
	orig_TS = TS
	while(True):
		if TS % 2 == 1:
			#print("TS: when odd",TS)
			break
		elif TS <= 1:
			#print("Less than 1")
			break
		else:
			TS = TS // 2
			mul *= 2
			#print("TS :",TS, "\nMul :",mul)
	print(orig_TS//mul)