import sys, functools

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = map(int,line.split()[1:])
		location = split[int(line.split()[0]) / 2]
		summed = functools.reduce(lambda x,y:x + abs(y - location), split, 0)
		print(summed)