s = input()
result = ""
for i in range(len(s)):
    found = False
    for j in range(len(result)):
        if s[i] == result[j]:
            found = True
            break
    if found == False:
        result += s[i]
print(result)