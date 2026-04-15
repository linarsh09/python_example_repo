def is_anagram(a, b):
    if len(a) != len(b):
        return False

    a = a.lower()
    b = b.lower()

    used = [False] * len(b)

    for i in range(len(a)):
        found = False
        for j in range(len(b)):
            if a[i] == b[j] and not used[j]:
                used[j] = True
                found = True
                break
        if not found:
            return False

    return True


s = input().split()

for i in range(len(s) - 1):
    if is_anagram(s[i], s[i+1]):
        print("YES")
    else:
        print("NO")
