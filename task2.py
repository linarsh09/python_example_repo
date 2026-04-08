def product(j):
    if j == 1:
        return 1 - 1 / (1 ** 2)
    return product(j - 1) * (1 - 1 / (j ** 2))


def summation(k):
    if k == 1:
        return product(1)
    return summation(k - 1) + product(k)


n = 2
print(summation(n))