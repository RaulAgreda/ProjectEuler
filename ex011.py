f = open("ex11.txt", "r")
lines = f.read().split("\n")
matrix = []
for line in lines:
	if (len(line) > 0):
		matrix.append(line.split())
		for i in range(len(matrix[-1])):
			matrix[-1][i] = int(matrix[-1][i])

largest = 0
for i in range(0, 20):
	for j in range(0, 20):
		total_r = 1
		total_c = 1
		total_d = 1
		total_d_i = 1
		for k in range(0, 4):
			if (i + k < 20):
				total_r *= matrix[i + k][j]
			if (j + k < 20):
				total_c *= matrix[i][j + k]
			if (i + k < 20 and j + k < 20):
				total_d *= matrix[i + k][j + k]
			if (i + k < 20 and j - k >= 0):
				total_d_i *= matrix[i + k][j - k]
		#print(f"({i}, {j})\n{total_r}, {total_c}, {total_d}")
		if (total_r > largest):
			largest = total_r
		if (total_c > largest):
			largest = total_c
		if (total_d > largest):
			largest = total_d
		if (total_d_i > largest):
			largest = total_d_i

for line in matrix:
	print(line)

print("Largest: " + str(largest))
