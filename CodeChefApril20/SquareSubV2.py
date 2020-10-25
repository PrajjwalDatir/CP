from sys import stdin


def give_me_output(seq, len_seq):
    # mul_list = [None]*len_seq
    mul_list = [seq[0]]
    if mul_list[0] % 4 != 2:  # mul_list[0] is 2,10,60,120
        ans = 1
    else:
        ans = 0
    for i in range(1, len_seq):  # seq is 2,5,6,2
        mul_list.append(seq[i] * mul_list[i - 1])  # mul_list is 2,10,60,120
    for i in range(1, len_seq):  # for i to 1 to 3 means 1,2,3
        # someNum = 1
        for j in range(i, len_seq):  # [1,2,3], [2,3], [3]
            if mul_list[j] // mul_list[i - 1] % 4 != 2:
                ans += 1
        if mul_list[i] % 4 != 2:
            ans += 1
    print(ans)


def square_sub():
    seq_size = int(stdin.readline())  # input size and sequence
    sequence = list(map(int, stdin.readline().split()))
    # need to find all consecutive combinations of the sequence
    give_me_output(sequence, seq_size)


T = int(stdin.readline())
for t in range(T):
    square_sub()
