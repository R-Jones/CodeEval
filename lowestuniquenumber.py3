import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		numbers = [int(x) for x in line.strip('\n').split()]
		filtered = [x for x in numbers if numbers.count(x) < 2]
		print(numbers.index(min(filtered)) + 1 if len(filtered) else 0)