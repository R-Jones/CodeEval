import sys, functools

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		print(functools.reduce(lambda x,y:x + (y if x[-1] != y else ''), line.strip('\n')))