
#C7_v2.py
"""
So we have to create two sets 
MUL = {a/p, b/q, c/r}
ADD = {a-p, b-q, c-r}
"""
import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	pqr = list(sys.stdin.readline().split())
	p = int(pqr[0])
	q = int(pqr[1])
	r = int(pqr[2])
	abc = list(sys.stdin.readline().split())
	a = int(abc[0])
	b = int(abc[1])
	c = int(abc[2])
	#print(p,q,r,a,b,c)
	#there are three solutions 1, 2 or 3
	#there are two ways either we can multiply or add
	#here ap means a-p
	#here AP means pa
	ap = a - p
	bq = b - q
	cr = c - r
	if p:
		AP = a / p
	else:
		AP = None
	if q:
		BQ = b / q
	else:
		BQ = None
	if r:
		CR = c / r
	else:
		CR = None
MUL = [AP, BQ, CR]
ADD = [ap, bq, cr]
