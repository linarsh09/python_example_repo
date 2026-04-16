def product(n):
    if n == 1:
        return 1 + 2/1
    return (1 + 2/n) * product(n - 1)

n = int(input())
print(product(n))