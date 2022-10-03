from src.is_prime import is_prime

def formula(n,a,b):
	return n*n + a*n + b

primes = set()

def is_prime_opt(n):
	if (n < 0):
		return 0
	if n not in primes:
		if (is_prime(n)):
			primes.add(n)
			return 1
		else:
			return 0
	return 1

max_ = 0
prod = 0

for a in range(-999, 1000):
	for b in range(-1000, 1001):
		n = 0
		while (is_prime_opt(formula(n, a, b))):
			n += 1
		if (n > max_):
			max_ = n
			prod = a * b

print(prod)
		