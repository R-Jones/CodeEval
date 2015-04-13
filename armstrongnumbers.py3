import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		spl = line.strip('\n')
		n = len(spl)
		print(int(spl) == sum([int(x) ** n for x in spl]))