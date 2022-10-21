# start with 1 next is at 2 distance four times, next is at 4 distance four times, next is at 6 distance and so on

n = 1
total = 1
it = 1
add = 2
while (add != 1001 + 1):
	n += add
	total += n
	if (it % 4 == 0):
		add+=2
	it+=1
print (total)