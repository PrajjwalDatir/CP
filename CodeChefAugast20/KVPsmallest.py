import sys

t = int(sys.stdin.readline())
def split(word): 
    return [char for char in word]  
# t=map(int,input().split())
for _ in range(t):
	s = sys.stdin.readline().rstrip()
	p = sys.stdin.readline().rstrip()
	n = len(s)
	m = len(p)
	s = ''.join(sorted(s))
	s = list(s)
	p = list(p)
	# print(s)
	# print(p)
	for i in p:
		# print(i)
		if i in s:
			s.remove(i)
	
	flag = True
	for i in range(n):
		if s[i] > p[0] and flag:
			print(*p, sep="",end="")
			flag = False
			break
		else:
			print(s[i],end="")
	print(*s[i:n],sep="")

	# print("final s :", s)
	# s.replace(p,"", 1)
	# print("final p :", p)