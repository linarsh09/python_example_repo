# #6
# s = 'dvalin'
# letters = 'aeiou'
# count = 0
# for char in s:
# 	if char in letters:
# 		count +=1
# print (count)
# 6
# n = 3
# x = 2
# def sum(n, x, prev=1, i=1):
# 	if i > n:
# 		return 0
# 	curr = prev * x/i
# 	return curr + sum(n, x, curr, i+1)
# print(sum(n, x))

string_my = input("Введите предложение")
words = []
current_word = ""

for char in string_my:
	if char.isalpha():
		current_word += char
	else:
		if current_word:
			words.append(current_word)
		current_word = ""
if current_word:
	words.append(current_word)

capital_words = []

for word in words:
	if "A" <= word[0] <= "Я":
		capital_words.append(word)
print(words)
