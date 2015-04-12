import sys

locOld = -1
replaceChar = '|'

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:

		split = line.split('C') if 'C' in line else line.split('_')

		locNew = len(split[0])

		if(locOld < 0):
			replaceChar = '|'
		elif(locNew > locOld):
			replaceChar = '\\'
		elif(locNew < locOld):
			replaceChar = '/'
		else:
			replaceChar = '|'

		locOld = locNew

		print(split[0] + replaceChar + split[1].strip('\n'))