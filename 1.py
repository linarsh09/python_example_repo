#5 вариант
str = input()
def solution(str):
	str_split = str.split(' ')
	res = ''

	for s in str_split:
		i = len(s) - 1
		while i >= 0:
			res += s[i]
			i -= 1
	return res

print(solution(str))


