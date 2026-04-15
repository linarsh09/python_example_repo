def Sum(n):
    if n == 0:
        return 0

    def element(k):
        return 1 / (2*k + 1)**2

    return element(n) + Sum(n-1)


n = int(input())
print(Sum(n))