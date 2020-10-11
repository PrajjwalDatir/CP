
# cook your dish here
import sys


test_cases = int(sys.stdin.readline().split())

for i_iter in range(test_cases):
    h, p = map(int, sys.stdin.readline().split())
    flag = False
    while p > 0:
        h -= p
        p = p//2
        if h < 0:
            flag = True
            break
    if h < 0 or flag:
        print("1")
    else:
        print("0")
