
import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	sec_line = list(sys.stdin.readline().split())
	NN = int(sec_line[0])
	KK = int(sec_line[1])
	Prices = list(sys.stdin.readline().split())
	#Prices[] size NN
	output = 0
	for i in range(NN):
		add = int(Prices[i]) - KK
		if add > 0:
			output += add
	print(output)