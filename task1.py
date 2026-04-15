#9вариант 
s = input()

words = s.split()
result = ""

for i in range(len(words)):
    result += words[i]
    if i != len(words) - 1:
        result += " "

print(result)