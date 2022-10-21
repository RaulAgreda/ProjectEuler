limit = 28123

def is_abundant(n):
	sum = 0
	i = 1
	while (i <= n/2):
		if (n % i == 0):
			sum += i
		i+=1
	return (sum > n)

total = 0
n = 1
abundants = set()
sums = set()
while (n < limit):
	if (n % 1000 == 0):
		print(n)
	if (n not in sums):
		total += n
	if (is_abundant(n)):
		abundants.add(n)
		for i in abundants:
			sums.add(i + n)
	n+=1
print(total)