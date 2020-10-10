
from sys import maxsize
from sys import stdin
count = int(stdin.readline())
result = []

for _ in range(count):
    start = list(map(lambda num: int(num), stdin.readline().split()))
    target = list(map(lambda num: int(num), stdin.readline().split()))

    diff = set()
    div = set()

    for i in range(len(start)):
        diff.add(target[i] - start[i])
        if start[i] != 0:
            div.add(target[i] / start[i])
        else:
            div.add(maxsize - i)

    unique = min(len(div), len(diff))

    if unique == 1:
        if 0 in diff or 0 in div:
            result.append('0')
        else:
            result.append('1')
    elif unique == 2:
        if 0 in diff or 0 in div:
            result.append('1')
        else:
            result.append('2')
    else:
        if start[2] * (target[0] - target[1]) + start[0] * (target[1] - target[2]) == start[1] * (target[0] - target[1]):
            result.append('2')
        else:
            result.append('3')

print(''.join(result))
