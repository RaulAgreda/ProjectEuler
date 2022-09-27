f = open("ex013.txt", "r")
numbers = [int(n) for n in f.read().split('\n')[:-1]]

print(str(sum(numbers))[0:10])
