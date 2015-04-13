import sys, functools

offset = 0
r = ['IIIVIIIX','XXXLXXXC','CCCDCCCM','MMM']


with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		rline = line[::-1]
		length = len(line.strip('\n'))

		outLine = []
		for place in range(0,length):
			num = int(rline[place])
			if(num in (4, 9)):
				outLine[:0] = r[place][]

		#functools.reduce(x + romanize(y, l), line.strip('\n'))
		#print([romanize(int(line[place]), place, offset)) for place in range(0,length)])