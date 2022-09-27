# 1 Jan 1900 -> Monday
# 30 days September, April, June and November: 	4, 6, 9, 11
# 31 days 										1, 3, 5, 7, 8, 10, 12
# days = 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def is_leap(y):
	return (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))

d30 = {4, 6, 9, 11}
d31 = {1, 3, 5, 7, 8, 10, 12}

def n_days(m, y):
	if (m in d30):
		return (30)
	elif (m in d31):
		return (31)
	return (29 if is_leap(y) else 28)

# 1 of January 1901 starts on twosday, so to count the sundays, we are checking if the days_cont is divisible by 7 with offset 1
days_count = 2
month = 1
year = 1901
sundays = 0
while (year != 2001):
	if (days_count % 7 == 0):
		sundays += 1
	days_count += n_days(month, year)
	month += 1
	if (month > 12):
		month = 1
		year+=1
print(sundays)
