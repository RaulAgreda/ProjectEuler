def generate_seq(n):
	terms = 0
	origin = n
	if (origin in checked):
		return (checked[origin])
	while (n != 1):
		if (n in checked):
			checked[origin] = terms + checked[n]
			return (checked[origin])
		n = int(n / 2 if n % 2 == 0 else 3*n + 1)
		terms+=1
	checked[origin] = terms + 1
	return (terms + 1)

i = 500000
max_s = 0
max_start = 0

checked = {}

while (i < 1000000):
	if (i not in checked):
		seq = generate_seq(i)
		if (max_s < seq):
			max_s = seq
			max_start = i
	i+=1
	
print(f"starting number: {max_start} with: {max_s} elements")
		
