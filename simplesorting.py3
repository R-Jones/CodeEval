import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		sortedStrings = ['%.3f' % x for x in sorted(map(float, line.strip('\n').split()))]
		print(' '.join(sortedStrings))