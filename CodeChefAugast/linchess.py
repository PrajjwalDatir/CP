import sys
test_cases = int(sys.stdin.readline())
# print(test_cases)
for i_iter in range(test_cases):
    new = list(map(int, sys.stdin.readline().split()))
    N = new[0]
    K = new[1]
    P = list(map(int, sys.stdin.readline().split()))
    mini = None
    location = P[0]
    for i in range(N):
        if not K % P[i]:
            if mini == None:
                mini = K/P[i]
                location = P[i]
            elif K/P[i] <= mini:
                mini = K/P[i]
                location = i
    if mini == None:
        print("-1")
    else:
        print(location)
