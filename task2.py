#9вариант 
def Sum(n):
    if n == 1:
        return (-1)**1 / ((2*1 + 1) * 1)

    def term(k):
        return (-1)**k / ((2*k + 1) * k)

    return term(n) + Sum(n - 1)


n = int(input())
print(Sum(n))