import sys, re

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		r = re.findall('0+ 0+', line)
		#result = ''.join(['1' * len(string[2:].strip()) for string in r if string[0:2] == '00'])
		result = map(lambda string:'1' * len(string[3:]) if string[:2] == '00' else string[2:], r)
		print(int(''.join(result), 2))