#5 вариант

def sum(n):
        def mult(j, k):
        	if j > k:
        		return 1
        	return (j + 1) * mult(j+1, k)
        if n == 1:
                return mult(1, 1)
        return mult(1, n) + sum(n - 1)

n = int(input("enter n: "))
print(sum(n))
