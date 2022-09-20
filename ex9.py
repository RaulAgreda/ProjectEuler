def pitagorian():
	a = 0
	while (a < 1000):
		b = a + 1
		while (b < 1000):
			c = b + 1
			while (c < 1000):
				if (a * a + b * b == c * c and a + b + c == 1000):
					return (a * b * c)
				c += 1
			b += 1
		a += 1
	return "error"

print(pitagorian())
