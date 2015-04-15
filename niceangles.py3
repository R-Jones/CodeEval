import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		sp = line.strip('\n').split('.')
		secs = 3600 * float('0.' + sp[1])
		print('{0}.{1}\'{2}"'.format(int(sp[0]), str(int(secs / 60)).rjust(2, '0'), str(int(secs % 60)).rjust(2, '0')))