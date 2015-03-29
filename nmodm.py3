import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(',')
		n = int(split[0])
		m = int(split[1])
		while(n >= m):
			n -= m
		print(n)