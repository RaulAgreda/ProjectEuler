mem = {}

def gen_path(x, y, dim):
	if ((x, y) in mem):
		return (mem[(x, y)])
	if (x > dim or y > dim):
		return 0
	if (x == dim and y == dim):
		return 1
	total = 0
	total += gen_path(x + 1, y, dim)
	total += gen_path(x, y + 1, dim)
	mem[(x, y)] = total
	return (total)

print(gen_path(0, 0, 20))
