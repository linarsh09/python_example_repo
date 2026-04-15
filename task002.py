import math

def factorial(k):
    if k == 0 or k == 1:
        return 1
    return k * factorial(k - 1)


def product(n, x):
    if n == 1:
        return 1 + math.sin(1 * x) / factorial(1)
    
    return product(n - 1, x) * (1 + math.sin(n * x) / factorial(n))


n = int(input("Введите n: "))
x = float(input("Введите x: "))

print(product(n, x))

