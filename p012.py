import sys

def n_divisors(n):
	i = 2
	total = 1
	while (i <= n):
		if (n % i == 0):
			total += 1
		i += 1
	return (total)

def nth_triangle(n):
	return (n * (n + 1) // 2)

def factorial(n):
	i = 1
	total = 1
	while (i <= n):
		total *= i
		i+=1
	return (total)

fact = factorial(500)
print(fact)
print(nth_triangle(int(sys.argv[1])))

i = 0
triangle = 0
while (True):
	triangle = nth_triangle(i)
	if (triangle > fact):
		print(triangle)
	i += 1