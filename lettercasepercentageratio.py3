import sys, functools

with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		capitals = functools.reduce(lambda x,y:x + y.istitle(), line.strip('\n'),0)
		percentage = capitals * 100 / float(len(line.strip('\n')))
		print('lowercase: ' + format(100.00 - percentage, '.2f') + ' ' + 'uppercase: ' + format(percentage, '.2f')) 