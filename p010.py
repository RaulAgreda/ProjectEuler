def is_prime(n):
	i = 2
	while (i <= n/i):
		if (n % i == 0):
			return (0)
		i+=1
	return (1)

n = 2
total = 0
last_prime = 2
while (n < 2000000):
	if (is_prime(n)):
		total += n
		last_prime = n
	n += 1

print(total)

