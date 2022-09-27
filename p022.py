fd = open("p022.txt", 'r')
names = fd.read().split('","')
fd.close()
names[0] = names[0][1:]
names[-1] = names[-1][:-1]

names.sort()
# ye python :v

def name_sum(name):
	total = 0
	for c in name:
		total += ord(c) - ord('A') + 1
	return (total)

total = 0
for i in range(len(names)):
	total += (i + 1) * name_sum(names[i])

print(total)
