def generate(k, A):
	if k == 1:
		st = ''
		for c in A:
			st += c
		comb.append(st)
	else:
		generate(k - 1, A)

		for i in range(k - 1):
			if k %2 == 0:
				A[i], A[k - 1] = A[k - 1], A[i]
			else:
				A[0], A[k - 1] = A[k - 1], A[0]
			generate(k - 1, A)

comb = []
generate(10, ['0','1','2','3','4','5','6','7','8','9'])
comb.sort()

print(comb[999999])