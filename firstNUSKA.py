s = input()

new_s = ''
for c in s:
    if c != ' ' :
        new_s += c.lower()


rev = ''
for c in new_s:
    rev = c + rev

if new_s == rev:
    print('Да')
else:
    print('Нет')









input()