# первая лаба
from math import e
def sum(k, n):
    def mult(j, k):
        if j > k:
            return 1
        return ((e ** (1 / j)) / j) * mult(j + 1, k)
    if k > n:
        return 0
    return mult(1, k) + sum(k + 1, n)
n = int(input("Введите n: "))
print(sum(1, n))