import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split(';')
		set1 = split[0].split(',')
		set2 = split[1].split(',')
		print(",".join(filter(lambda x: x in set2, set1)))