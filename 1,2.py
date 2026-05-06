def find_longest(s):
    max_sub = ""
    current_sub = ""
    for char in s:
        if char in current_sub:
            index = current_sub.find(char)
            current_sub = current_sub[index + 1:]
        current_sub += char
        if len(current_sub) > len(max_sub):
            max_sub = current_sub
    return max_sub

def get_sum(k):
    if k == 1:
        return -1.0
    return ((-1)**k / k**2) + get_sum(k - 1)

def get_product(n):
    if n == 1:
        return get_sum(1)
    return get_sum(n) * get_product(n - 1)

input_str = input("Введите строку: ")
sub = find_longest(input_str)
print("Подстрока:", sub)
print("Длина:", len(sub))

n_val = int(input("Введите число n: "))
if n_val > 0:
    print("Результат P:", get_product(n_val))