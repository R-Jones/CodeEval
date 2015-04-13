import sys

currentnum = None

count = 1

outline = []

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		outline = []
		currentnum = None
		for char in line.split() + ['\n']:
			if(char == currentnum):
				count += 1
			elif(currentnum == None):
				currentnum = char
			else:
				outline += [str(count) + ' ' + currentnum]
				currentnum = char
				count = 1
		print(' '.join(outline))
