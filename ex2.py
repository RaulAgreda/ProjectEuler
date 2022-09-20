n1 = 1
n2 = 2
prev = 0
total = 0

while (n2 < 4000000):
	if (n2 % 2 == 0):
		total += n2
	prev = n2
	n2 = n2 + n1
	n1 = prev
print (total)
