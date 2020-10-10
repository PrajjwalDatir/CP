# jug2.py
import sys
N, K = map(int, sys.stdin.readline().split())
string = sys.stdin.readline()
def solve(N, K, string):
	count = 0
	maxm = 0

	for count in range(N - K):
		print(set(string[count:count + K + 1]))
		temp= len(set(string[count:count + K + 1]))
		print(temp)
		if temp > maxm:
			maxm = temp
	print(maxm)

solve(N , K , string)



