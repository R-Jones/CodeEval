import sys


counters = []
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		counters = [0] * len(line.strip('\n'))
		for char in line.strip('\n'):
			counters.append(0)
			#counters[int(char)]++