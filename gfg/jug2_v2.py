
n, k = map(int, input().split())
string = input()

arr = [0] * 26

for i in range(k):
    arr[ord(string[i]) - ord('a')] += 1

final_ans = 0
for i in range(26):
    if arr[i]:
        final_ans += 1
final_ans2 = final_ans
# lenn = len(string)
for i in range(k, n):

	temp_ans2 = 0
    if arr[ord(string[i]) - ord('a')]  == 0:
    	temp_ans2 += 1
    arr[ord(string[i]) - ord('a')] += 1
    
    if arr[ord(string[i - k]) - ord('a')] == 1:
    	temp_ans2 -= 1
    arr[ord(string[i - k]) - ord('a')] -= 1

    temp_ans = 0
    for i in range(26):
        if arr[i]:
            temp_ans += 1
    final_ans = max(temp_ans, final_ans)

final_ans = max(final_ans, temp_ans)

print(final_ans)
