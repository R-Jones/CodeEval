import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		sum = 0
		for c in line.strip('\n'):
			sum+=int(c)
		print(sum)
