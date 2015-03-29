import sys
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		print(line.split()[-2])