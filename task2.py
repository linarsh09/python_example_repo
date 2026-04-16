import math

def factorial(k):
	if k == 0 or k == 1:
		return 1
	return k * factorial(k - 1)
def calculate_product(k, n, x):
	if k > n:
		return 1
	
	term = (1 + math.sin(k * x))/factotial(k)
	return term * calculate_product(k + 1, n, x)
n = 3
x = 1.0
result = calculate_product(1, n, x)
print(result)

	
