import sys, functools

def gap(row):
	left = row.rfind('X')
	right = row.find('Y')
	return right - left - 1

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(',')
		print(functools.reduce(lambda x, y: min(x, gap(y)), line.split(','), sys.maxsize))
