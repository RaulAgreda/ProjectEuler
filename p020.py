def factorial(n):
	i = 1
	total = 1
	while (i <= n):
		total *= i
		i+=1
	return (total)

num = str(factorial(100))
total = 0

for digit in num:
	total += int(digit)

print(total)