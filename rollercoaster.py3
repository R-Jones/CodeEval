import sys, functools


def flipCase(string, char):
	global counter
	if not(char.isalpha()):
		return string + char
	else:
		counter += 1
		return string + (char.lower() if counter % 2 == 0 else char.upper())


with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		counter = 0
		print(functools.reduce(flipCase,line.strip('\n'),''))