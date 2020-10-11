from sys import stdin


T = int(stdin.readline())
for _ in range(T):
    seq_size = int(stdin.readline())
    # pass all the combination of given sequence
    sequence = list(map(int, stdin.readline().split()))
    mul_arr = [None]*seq_size
    cnt = 0
    for i in range(0, seq_size):
        mul_arr[i] = abs(sequence[i]) % 4
    # print(mul_arr)
    for my_iter in range(seq_size):
        for i in range(my_iter, seq_size):
            if mul_arr[i] == 0:
                cnt = cnt + seq_size - i
                break
            elif mul_arr[i] == 1:  # 0 2 1 1 1 1 3 3
                cnt += 1  # 8 + 6 + 5 + 4 + 3 + 2 + 1
            elif mul_arr[i] == 3:
                cnt += 1
            elif mul_arr[i] == 2:
                while i < seq_size - 1:
                    i += 1
                    if mul_arr[i] == 2 or mul_arr[i] == 0:
                        cnt = cnt + seq_size - i
                        break
                break
    print(cnt)
