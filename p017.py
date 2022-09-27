ref = {
	0: "",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "onethousand"
}

def c_2digits(n):
	total = 0
	if (n in ref):
		print(ref[n], end = '')
		return (len(ref[n]))
	print(ref[n // 10 * 10], end = ' ')
	total += len(ref[n // 10 * 10])
	print(ref[n % 10], end = '')
	total += len(ref[n % 10])
	return total

def c_3digits(n):
	total = 0
	print (ref[n // 100], end = ' ')
	total += len(ref[n // 100])
	print (ref[100], end = ' ')
	total += len(ref[100])
	if (n % 100 != 0):
		print("and ", end = '')
		total += c_2digits(n % 100) + 3
	return total

total = 0
i = 1

while (i < 1000):
	print (f"{i}: ", end = '')
	if (i in ref and i < 100):
		print(ref[i], end = '')
		total += len(ref[i])
	elif (i < 100):
		total += c_2digits(i);
	else:
		total += c_3digits(i);
	print("")
	i += 1

print("1000: one thousand")
total += len(ref[1000])
print(total)