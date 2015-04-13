import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split(',')
		fruit = [item for item in split if not item.isdigit()]
		numbers = [item for item in split if item.isdigit()]
		print(",".join(fruit) + ('|' if len(fruit) * len(numbers) > 0 else '') + ','.join(numbers))