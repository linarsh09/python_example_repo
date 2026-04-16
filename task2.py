#9вариант 
def f(n):
    if n == 1:
        return (-1)**1 / ((2*1 + 1) * 1)
    return f(n - 1) + (-1)**n / ((2*n + 1) * n)

n = int(input())
print(f(n))