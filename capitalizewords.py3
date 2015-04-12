import sys, functools

previousChar = ' '

def charPress(line, char):
	global previousChar
	if previousChar == ' ':
		char = char.upper()
	previousChar = char
	return line + char


with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		previousChar = ' '
		print(functools.reduce(charPress, line.strip('\n'), ''))