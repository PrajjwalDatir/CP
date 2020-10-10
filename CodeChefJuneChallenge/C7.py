
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
		AP = 0
	if q:
		BQ = b / q
	else:
		BQ = 0
	if r:
		CR = c / r
	else:
		CR = 0
	cnt = 3
# check for p q r 0 conditions
	# use this  isinstance(,int)
	if((ap == bq) and (bq == cr)):
		if(ap == 0):
			cnt = 0
		else:
			cnt = 1
	elif(( AP == BQ) and (BQ == CR )):
		if( AP == 1):
			cnt = 0
		else:
			cnt = 1
	elif( AP == BQ) or (AP == CR) or (BQ == CR):
		if(AP == 1) or (BQ == 1) or (CR == 1):
			cnt = 1
		else:
			cnt = 2
	elif((ap == bq) or (ap == cr) or (bq == cr)):
		if(ap == 0) or (bq == 0) or (cr == 0):
			cnt = 1
		else:
			cnt = 2
	elif True:
		if p:
			mod1 = a % p
		else:
			mod1 = a
		if q:
			mod2 = b % q
		else:
			mod2 = b		
		if r:
			mod3 = c % r
		else:
			mod3 = c
		if (mod1 == mod2) and (mod2 == mod3):
			cnt = 2
	#elif(is_check(a,b,c,p,q,r)):
	#	cnt =  2
	else:
		cnt = 3
	print(cnt)