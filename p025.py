x1 = 1
x2 = 1
res = 0
index = 2

limit = 10**999

while (res < limit):
	res = x1 + x2
	x1 = x2
	x2 = res
	index += 1

print(index)
