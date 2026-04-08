def sum(n):
    if n==0:
        return 0
    return 1/n + sum(n-1)

result = sum(3)
print(result)