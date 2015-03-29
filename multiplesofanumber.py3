import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(',')
		multiple = int(split[1])
		target = int(split[0])
		while True:
			if multiple >= target:
				print(multiple)
				break
			else:
				multiple += int(split[1])
