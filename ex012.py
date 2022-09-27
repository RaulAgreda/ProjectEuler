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
	total = 0
	for i in range(1, n + 1):
		total += i
	return (total)

def factorial(n):
	i = 1
	total = 1
	while (i <= n):
		total *= i
		i+=1
	return (total)

fact = factorial(500)
i = 2
triangle = 1
while (triangle < fact):
	#print(triangle)
	if (n_divisors(i) > 500):
		print(triangle)
		break
	triangle += i
	i += 1

