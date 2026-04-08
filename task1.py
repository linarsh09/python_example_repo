#1 variant
s = input()
words = s.split( )
letters = []
for word in words:
    letters.append(len(word))
        
max_l = letters[0]
idx = 0
for i in range(len(letters)):
    if letters[i] > max_l:
        max_l = letters[i]
        idx = i
   
print (words[idx])