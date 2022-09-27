def is_evenly_divisible(n):
	for i in range(2, 21):
		if (n % i != 0):
			return (0)
	return (1)

n = 20
while (1):
	if (is_evenly_divisible(n)):
		print(n)
		break
	n+=20
