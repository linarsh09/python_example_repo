# 6
n = 3
x = 2
def sum(n, x, prev=1, i=1):
	if i > n:
		return 0
	curr = prev * x/i
	return curr + sum(n, x, curr, i+1)
print(sum(n, x))