import sys


with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:

		currentMaxString = ''
		for word in line.strip('\n').split():
			if len(word) > len(currentMaxString):
				currentMaxString = word
		print(currentMaxString)