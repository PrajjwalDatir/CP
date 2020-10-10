# N^2 = 
# 3^2 = 1+2+3+2+1
# (n - 1)^2 = n^2 - 2n + 1
# n^2 = (n - 1)^2 - 2n + 1
# f(n^2) = f((n - 1))^2 + 2n - 1
def func(N):
	if N == 1:
		return 1
	else:
		return func(N - 1) + (2 * N) - 1

print(func(10))