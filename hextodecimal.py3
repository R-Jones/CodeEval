import sys

with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		print(int(line.strip('\n'), 16))