import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(',')
		print(split[0].rfind(split[1][0]))