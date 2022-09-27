def is_prime(n):
	i = 2
	while (i <= n/i):
		if (n % i == 0):
			return (0)
		i+=1
	return (1)

n = 2
nth = 0
while (nth != 10001):
	if (is_prime(n)):
		nth += 1
	n += 1

print(n - 1)

