import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		days = [int(x) for x in line.strip('\n').split(';')[1].split()]
		span = int(line.split(';')[0])
		print(max([sum(days[x:x+span]) for x in range(0,len(days) - span + 1)] + [0]))