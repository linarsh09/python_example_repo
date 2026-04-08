def Sum(n):
    if n == 0:
        return 0
    def multiply(n):
        if n == 0:
            return 1
        return 1/(n+1) * multiply(n-1)
    return multiply(n) + Sum(n-1)
n = int(input())    
example = Sum(n)
print(example)