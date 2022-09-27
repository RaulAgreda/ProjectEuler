def is_prime(n):
	i = 2
	while (i <= n / i):
		if (n % i == 0):
			return (0)
		i+=1
	return (1)

def next_divisor(n, div):
	i = div + 1
	while (i < n):
		if (n % i == 0):
			return (i)
		i+=1

div = 1

while (1):
	div = next_divisor(600851475143, div)
	if (is_prime(600851475143 / div)):
		print(600851475143 / div)
		break

