#8 variant
def rle_metod(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1]
            if count > 1:
                result += str(count)
            count = 1

    result += s[-1]
    if count > 1:
        result += str(count)

    return result


s = input()
print(rle_metod(s))