from re import I


def d(n):
	total = 1
	i = 2
	while (i <= n // 2):
		if (n % i == 0):
			total += i
		i+=1
	return (total)

i = 1
sum = 0
amicable = set()
while (i <= 10000):
	b = d(i)
	if (i != b and d(b) == i):
		amicable.add(i)
		amicable.add(b)
	i+=1

for n in amicable:
	sum += n

print(amicable)
print(sum)