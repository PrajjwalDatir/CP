import sys
import math


def primeFactors(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = n / i
            count += 1
    if n > 2:
        count += 1
    return count


for _ in range(int(sys.stdin.readline())):
    x, k = map(int, sys.stdin.readline().split())
    if x == 1:
        if k == 0:
            print("1")
        else:
            print("0")
    elif k <= primeFactors(x):
        print(1)
    else:
        print(0)
