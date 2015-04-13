import sys, re

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		cc = ''.join([str(line.count(str(x))) for x in range(0, len(line.strip('\n')))])
		print(int(cc == line.strip('\n')))