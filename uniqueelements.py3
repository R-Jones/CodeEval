import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split(',')
		for x in range(len(split) - 1, 0, -1):
			if split[x] == split[x - 1]:
				split.pop(x)
		print(",".join(split))