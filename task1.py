#variant 4 tukusheva
def recur(n):
    z=n
    if n == 1:
        return 1
    def proiz(i):
        r = -1**(i+1)
        return r
    return ((proiz(n) / z)*proiz(n-1)) + recur(n-1)

res=recur(4)
print(res)