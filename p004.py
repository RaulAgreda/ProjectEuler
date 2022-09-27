import sys

def is_palindrome(n):
	a = str(n)
	for i in range(len(a) // 2):
		if (a[i] != a[len(a) - 1 - i]):
			return (0)
	return (1)

n1 = 100
maxvalue = 0

while (n1 < 1000):
	n2 = 100
	while (n2 < 1000):
		result = n1 * n2
		if (is_palindrome(result) and result > maxvalue):
			maxvalue = result
		n2 += 1
	n1 += 1

print(maxvalue)
