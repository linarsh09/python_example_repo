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
	