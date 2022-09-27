class MaxTrianglePath:
	def __init__(self, file):
		self.cache = {}
		self.M = self._extract_matrix(file)

	def _extract_matrix(self, file):
		matrix = []
		fd = open(file, 'r')
		lines = fd.read().split('\n')
		fd.close()
		for i in range(len(lines)):
			nums = lines[i].split(' ')
			matrix.append([])
			for n in nums:
				matrix[i].append(int(n))
		return (matrix)

	def get_path(self, level, position):
		if ((level, position) in self.cache):
			return self.cache[(level, position)]
		if (level == len(self.M) - 1):
			return self.M[level][position]
		total = self.M[level][position]
		total1 = total + self.get_path(level + 1, position)
		total2 = total + self.get_path(level + 1, position + 1)
		self.cache[(level, position)] = total1 if total1 > total2 else total2
		return self.cache[((level, position))]

if (__name__ == "__main__"):
	print(MaxTrianglePath("p018.txt").get_path(0, 0))