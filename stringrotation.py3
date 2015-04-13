import sys, functools

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		s = line.strip('\n').split(',')
		print(functools.reduce(lambda x,y:x | (s[1][y:] + s[1][:y] == s[0]), range(0, len(s[1])), False))