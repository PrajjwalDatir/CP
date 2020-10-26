T = int(input())
for _ in range(T):
    N= int(input())
    arr = list(map(int, input().split(" ")))
    odd = 0
    even = 0
    for i in range(N):
        if i%2:
            odd += arr[i]
        if not i%2:
            even += arr[i]
    if odd > even:
        print(odd)
    else:
        print(even)