import sys

def unfurl(matrix, n, m, depth):
	shell = []
	if(depth * 2 + 1 == n):
		if(depth * 2 + 1 == m):
			return [matrix[depth][depth]]
		else:
			return matrix[depth]
	elif(depth * 2 + 1 == m):
		return [matrix[i][depth] for i in range(depth, n - depth)]

	shell += matrix[depth][depth:-depth - 1]
	shell += [matrix[i][-depth - 1] for i in range(depth, n - depth - 1)]
	shell += [matrix[-depth - 1][i] for i in range(m - depth - 1, depth, -1)]
	shell += [matrix[i][depth] for i in range(n - depth - 1, depth, -1)]

	if((depth + 1) * 2 == n or (depth + 1) * 2 == m):
		return shell
	return shell + unfurl(matrix, n, m, depth + 1)

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split(';')
		lst = split[2].split()
		n = int(split[0])
		m = int(split[1])
		matrix = [[lst[j * m + i] for i in range(m)] for j in range(n)]
		print(' '.join(unfurl(matrix, n, m, 0)))