n = 10**100000
max_ = 0

# Guardar en cache un número con el primer índice para comparar cuando puede empezar el ciclo

def check_loop(ns):
	counter = 0
	j = 0
	repeat = False
	for i in range(1, len(ns)):
		if (counter > len(ns) - i):
			print("break")
			return (0)
		counter += 1
		if (ns[i] == ns[0] and ns[i + 1] == ns[1]):
			if (ns[0:counter] == ns[i:i+counter]):
				return (counter)

	return (0)

d = 1
while (d < 1000):
	print(d)
	counter = 0
	ns = str(n//d)
	l = check_loop(ns) if len(ns) > 1000 else 0
	if (l > max_):
		max_ = l
	# print(l)
	d+=1

print(max_)