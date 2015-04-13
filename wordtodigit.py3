import sys

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		print(''.join([str(words.index(x)) for x in line.strip('\n').split(';')]))