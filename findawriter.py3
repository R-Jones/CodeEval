import sys
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split('|')
		if(len(split) != 2):
			continue
		outLine = ''
		for x in split[1].split():
			outLine+=split[0][int(x) - 1]
		print(outLine)