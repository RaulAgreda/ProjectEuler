solutions = []
n = 5
npowers = {}
for i in range(0, 10):
	npowers[i] = i ** n

def find_number(number, add):
	if (len(number) == 6):
		if str(add) == number:
			solutions.append(add)
		return
	for i in range(0, 10):
		find_number(number + str(i), add + npowers[i])

find_number("", 0)
print(solutions)
print(sum(solutions))
		