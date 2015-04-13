import sys

letters = 'abcdefghij'

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		result = ''.join([str(letters.index(x)) if x in letters else x if str.isdigit(x) else '' for x in line.strip()])
		print(result if result else 'NONE')