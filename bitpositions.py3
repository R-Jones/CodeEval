import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(',')
		n = int(split[0])
		p1 = int(split[1]) - 1
		p2 = int(split[2]) - 1
		if ((n >> p1) % 2 == (n >> p2) % 2):
			print('true')
		else:
			print('false')