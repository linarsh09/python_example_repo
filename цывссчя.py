def Sum(n):
    if n == 1:
        return 1

    def multiply(n):
        if n == 1:
            return 1
        return (1 / n) * multiply(n - 1)

    return multiply(n) + Sum(n - 1)


n = int(input())
example = Sum(n)
print(example)